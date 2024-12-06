import tkinter as tk
import subprocess

def create_result_window(answer):
    result_root = tk.Tk()
    result_root.title("結果")
    result_root.attributes('-fullscreen', True)  # 全画面表示を有効にする

    if answer == "金沢市":
        result_text = "正解です！"
    else:
        result_text = "不正解です。"

    result_label = tk.Label(result_root, text=result_text, font=("Arial", 50), bg="blue", fg="white")
    result_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def open_title():
        subprocess.Popen(['python', 'title.py'])
        result_root.destroy()  # ウィンドウを閉じる

    def open_review():
        subprocess.Popen(['python', 'review.py'])
        result_root.destroy()  # ウィンドウを閉じる

    # ここでボタンを追加して、それぞれの関数を呼び出すようにします
    title_button = tk.Button(result_root, text="タイトルに戻る", command=open_title, font=("Arial", 14))
    title_button.place(relx=0.3, rely=0.7, anchor=tk.CENTER)

    review_button = tk.Button(result_root, text="復習する", command=open_review, font=("Arial", 14))
    review_button.place(relx=0.7, rely=0.7, anchor=tk.CENTER)

    result_root.mainloop()
