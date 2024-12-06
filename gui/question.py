import tkinter as tk
import subprocess
from result import create_result_window  # `result` モジュールから関数をインポート

# 前回の解答を保存する変数
previous_answer = ""


def a():
    global previous_answer

    root = tk.Tk()
    root.title("QA")
    root.attributes('-fullscreen', True)  # 全画面表示を有効にする

    label = tk.Label(root, text="問題", font=("Arial", 50), bg="blue", fg="white")
    label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    label2 = tk.Label(root, text="石川の県庁所在地はどこでしょう", font=("Arial", 20), bg="blue", fg="white")
    label2.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

    answer_label = tk.Label(root, text="解答を入力してください:", font=("Arial", 14))
    answer_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    answer_entry = tk.Entry(root, font=("Arial", 14), width=30)
    answer_entry.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
    answer_entry.insert(0, previous_answer)

    def submit_answer():
        global previous_answer
        previous_answer = answer_entry.get()
        root.destroy()
        create_result_window(previous_answer)

    submit_button = tk.Button(root, text="送信", command=submit_answer, font=("Arial", 14))
    submit_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    root.mainloop()

a()
