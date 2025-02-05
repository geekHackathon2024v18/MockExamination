import json
import csv
import threading
import time
import base64
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import google.generativeai as genai

# ✅ Google Gemini API のキーを設定
API_KEY = "AIzaSyDAUhLHSPXjYWCVqAAWTMOxTh6aJ8DolMY"  # 🔹 ここに自分のAPIキーを入力してください

def select_png_file():
    """📂 ユーザーにPNGファイルを選択させる"""
    file_path = filedialog.askopenfilename(
        title="PNGファイルを選択してください",
        filetypes=[("PNG Files", "*.png")]
    )
    return file_path

def compress_image(image_path, output_path="compressed.jpg", quality=50):
    """📉 画像を圧縮してJPEGに変換（ファイルサイズ削減）"""
    img = Image.open(image_path)
    img = img.convert("RGB")  # PNGをJPEG形式に変換
    img.save(output_path, "JPEG", quality=quality)
    return output_path

def encode_image(image_path):
    """📸 画像をBase64にエンコード"""
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

def save_to_csv(data, filename="quiz.csv"):
    """✅ 生成した問題をCSVファイルに保存"""
    if "question_list" not in data or not data["question_list"]:
        print("❌ エラー: 生成された問題がありません。")
        return
    
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["question_sentence", "choice_1", "choice_2", "choice_3", "choice_4", "answer","explanation"])
        
        for question in data["question_list"]:
            writer.writerow([
                question["question_sentence"],
                question["choice_1"],
                question["choice_2"],
                question["choice_3"],
                question["choice_4"],
                question["answer"],
                question["explanation"]
                
            ])
    
    print(f"✅ 問題が {filename} に保存されました！")

def request_gemini_from_png():
    """🎯 選択したPNGから問題を生成し、CSVに保存する"""
    png_path = select_png_file()
    if not png_path:
        print("❌ ファイルが選択されませんでした。処理を中止します。")
        return None

    print(f"📂 選択されたPNG: {png_path}")

    # 画像を圧縮
    compressed_image = compress_image(png_path)
    print(f"📉 画像を圧縮しました: {compressed_image}")

    # 画像をBase64にエンコード
    encoded_image = encode_image(compressed_image)

    # ✅ Google Gemini API の設定
    genai.configure(api_key="AIzaSyDAUhLHSPXjYWCVqAAWTMOxTh6aJ8DolMY")

    # 🔹 画像を含むプロンプトを作成
    prompt_text = """
    授業の模擬的なテスト問題をjson形式で生成してください。
    画像の内容を基に、3~10問の4択問題を作成してください。
    JSONのフォーマット:
    ```json
    {
      "mock_examination_name": "string",
      "question_list": [
        {
          "question_sentence": "string",
          "choice_1": "string",
          "choice_2": "string",
          "choice_3": "string",
          "choice_4": "string",
          "answer": "string"
          "explanation": "string"
        }
      ]
    }
    ```
    """

    model = genai.GenerativeModel('gemini-1.5-flash')  # ✅ 画像を扱うモデルを使用

    max_retries = 3
    for i in range(max_retries):
        try:
            print("📝 Gemini にリクエストを送信中... (試行 {} 回目)".format(i + 1))
            result = model.generate_content(
                contents=[  # ✅ 正しいリクエストフォーマット
                    {
                        "parts": [
                            {"text": prompt_text},
                            {"inline_data": {"mime_type": "image/jpeg", "data": encoded_image}}
                        ]
                    }
                ],
            )
            if result.text.strip():
                break  # 成功したらループを抜ける
        except Exception as e:
            print(f"⚠️ Gemini APIのエラー: {e}")
            if i < max_retries - 1:
                print("🔄 再試行します...")
                time.sleep(5)
            else:
                print("❌ APIリクエストが失敗しました。")
                return None

    print("✅ Gemini APIの応答を受信")
    print(result.text)  # 🔍 これでレスポンスの内容を確認

    try:
        json_data = result.text.replace('```json', '').replace('```', '')
        data = json.loads(json_data)
    except json.JSONDecodeError as e:
        print("❌ JSONの解析に失敗しました:", e)
        return None

    save_to_csv(data, "quiz.csv")
    return data

def create_window():
    """🖥️ PNGを選択し、クイズを生成するGUI"""
    root = tk.Tk()
    root.title("PNGからクイズ生成")
    root.attributes('-fullscreen', True)
    root.configure(bg="white")

    label = tk.Label(root, text="PNGを選択してクイズを作成", font=("Arial", 30), bg="white", fg="black")
    label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

    def process_png():
        """🔄 別スレッドで PNG を処理（GUIフリーズ防止）"""
        def task():
            exam_data = request_gemini_from_png()
            if exam_data:
                messagebox.showinfo("完了", "クイズが quiz.csv に保存されました！")
            else:
                messagebox.showerror("エラー", "クイズの生成に失敗しました。")

        threading.Thread(target=task).start()  # 🔄 非同期処理を実行

    select_button = tk.Button(root, text="PNGを選択", command=process_png, font=("Arial", 20))
    select_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def back_to_title():
        """🔙 タイトル画面に戻る"""
        root.destroy()
        from gui.title import open_title_window
        open_title_window(None)

    title_button = tk.Button(root, text="タイトルに戻る", command=back_to_title, font=("Arial", 14))
    title_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    root.mainloop()

if __name__ == "__main__":
    create_window()
