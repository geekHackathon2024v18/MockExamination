import sys
import tkinter as tk
import subprocess
import csv
def create_result_window(answer, correct_answer, explanation):
    result_root = tk.Tk()
    result_root.title("結果")
    result_root.attributes('-fullscreen', True)

    if answer == correct_answer:
        result_text = f"正解です！\n\n{explanation}"
    else:
        result_text = f"不正解です。\n\n{explanation}"

    result_label = tk.Label(result_root, text=result_text, font=("Arial", 30), bg="blue", fg="white")
    result_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def open_title():
        result_root.destroy()  # ウィンドウを閉じる
        subprocess.Popen(['python', 'src/gui/title.py'])

    def open_review():
        result_root.destroy()  # ウィンドウを閉じる
        subprocess.Popen(['python', 'src/gui/review.py'])

    def continue_quiz():
        if not load_quiz_data('src/gui/quiz.csv'):  # クイズがなくなった場合
            result_text = "問題がありません"
            result_label.config(text=result_text)
            result_root.after(2000, open_title)  # 2秒後にタイトルに戻る
        else:
            subprocess.Popen(['python', 'src/gui/question.py'])  # 次のクイズを表示
            result_root.destroy()

    def load_quiz_data(filename):
        quiz_list = []
        try:
            with open(filename, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # ヘッダーをスキップ
                quiz_list = list(reader)
        except FileNotFoundError:
            print("クイズデータファイルが見つかりません")
        return quiz_list

    # ボタンの作成と配置
    title_button = tk.Button(result_root, text="タイトルに戻る", command=open_title, font=("Arial", 14))
    title_button.place(relx=0.2, rely=0.7, anchor=tk.CENTER)

    review_button = tk.Button(result_root, text="復習する", command=open_review, font=("Arial", 14))
    review_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    if load_quiz_data('src/gui/quiz.csv'):
        continue_button = tk.Button(result_root, text="続けて解く", command=continue_quiz, font=("Arial", 14), bg="green", fg="white")
        continue_button.place(relx=0.8, rely=0.7, anchor=tk.CENTER)

    result_root.mainloop()

# コマンドライン引数から選択した答えと正しい答えと解説を取得
if __name__ == "__main__":
    selected_answer = sys.argv[1]
    correct_answer = sys.argv[2]
    explanation = sys.argv[3]
    create_result_window(selected_answer, correct_answer, explanation)
