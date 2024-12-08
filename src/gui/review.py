import tkinter as tk
import csv
import subprocess

# 解いた問題を読み込む
def load_answered_quizzes(filename):
    answered_quizzes = []
    try:
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            answered_quizzes = list(reader)
    except FileNotFoundError:
        print("解いた問題のファイルが見つかりません")
    return answered_quizzes

# 解いた問題をリセットして quiz.csv に戻す
def reset_answered_quizzes():
    answered_quizzes = load_answered_quizzes('src/gui/answered_quizzes.csv')

    # quiz.csv に解いた問題を追加
    with open('src/gui/quiz.csv', 'a', newline='', encoding='utf-8') as quizfile:
        writer = csv.writer(quizfile)
        writer.writerows(answered_quizzes)

    # answered_quizzes.csv を空にする
    with open('src/gui/answered_quizzes.csv', 'w', newline='', encoding='utf-8') as f:
        pass

    # リセット完了メッセージ
    reset_message = tk.Label(root, text="解いた問題をリセットしました", font=("Arial", 16), bg="white", fg="black")
    reset_message.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

# tkオブジェクトの作成
root = tk.Tk()
root.title("復習")  # ウィンドウのタイトルを設定
root.attributes('-fullscreen', True)  # 全画面表示を有効にする

# 解いた問題のリストを読み込む
answered_quizzes = load_answered_quizzes('answered_quizzes.csv')

if not answered_quizzes:
    # 解いた問題がない場合
    no_quizzes_label = tk.Label(root, text="解いた問題がありません", font=("Arial", 50), bg="red", fg="white")
    no_quizzes_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
else:
    # 解いた問題を表示する
    for i, quiz in enumerate(answered_quizzes):
        question_label = tk.Label(root, text=f"問題 {i+1}: {quiz[0]}", font=("Arial", 16))
        question_label.pack(pady=10)
        for j in range(1, 5):
            choice_label = tk.Label(root, text=f"選択肢 {j}: {quiz[j]}", font=("Arial", 14))
            choice_label.pack(pady=5)

def open_title():
    subprocess.Popen(['python', 'src/gui/title.py'])
    root.withdraw()  # 現在のウィンドウを閉じる

# タイトルに戻るボタン
title_button = tk.Button(root, text="タイトルに戻る", command=open_title, font=("Arial", 14))
title_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

# リセットボタン
reset_button = tk.Button(root, text="問題をリセットする", command=reset_answered_quizzes, font=("Arial", 14), bg="white", fg="black")
reset_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

# メインループの実行
root.mainloop()