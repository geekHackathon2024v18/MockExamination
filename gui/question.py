import tkinter as tk
import csv
import random
import subprocess

from data.database.sql_alchemy_control import SqlAlchemyControl



# グローバル変数の定義
quiz_list = []
choice4_list = []
answered_quizzes = []  # 解いた問題を記録するリスト
choice_var = None
root = None
current_quiz = None

# CSVファイルからクイズデータを読み込む
def load_quiz_data(filename):
    global quiz_list, answered_quizzes
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # ヘッダーをスキップ
        quiz_list = list(reader)

    # 解いた問題を読み込んでリストに追加
    try:
        with open('gui/answered_quizzes.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            answered_quizzes = list(reader)
    except FileNotFoundError:
        answered_quizzes = []

    # 解いた問題をクイズリストから除外
    quiz_list = [quiz for quiz in quiz_list if quiz not in answered_quizzes]

def load_quiz_data(mock_examination_id: int) -> None:
    db = SqlAlchemyControl()
    global quiz_list, choice4_list, answered_quizzes
    quiz_list = db.read.question(mock_examination_id=mock_examination_id)
    # uiが4択固定なんで、このタイミングで読み出す
    choice4_list = db.read.choice4(mock_examination_id=mock_examination_id)


# クイズを表示するウィンドウを作成
def create_quiz_window():
    global choice_var, root, current_quiz
    if len(quiz_list) == 0:
        show_no_quiz_message()
        return

    root = tk.Tk()
    root.title("4択クイズ")
    root.attributes('-fullscreen', True)

    current_quiz = random.choice(quiz_list)  # ランダムにクイズを選択
    for choice4 in choice4_list:
        if choice4.question_id == current_quiz.id:
            current_choice4 = choice4
            break

    # 質問ラベルの作成
    question_label = tk.Label(root, text=current_quiz.question_sentence, font=("Arial", 30))
    question_label.pack(pady=20)

    # 選択肢のラジオボタンを作成
    choice_var = tk.StringVar()
    choice_var.set(None)  # 初期値を設定

    # 選択肢1～4をラジオボタンとして追加
    tk.Radiobutton(root, text=current_choice4.choice_1, variable=choice_var, value="1", font=("Arial", 30)).pack(anchor=tk.W, padx=20)
    tk.Radiobutton(root, text=current_choice4.choice_2, variable=choice_var, value="2", font=("Arial", 30)).pack(anchor=tk.W, padx=20)
    tk.Radiobutton(root, text=current_choice4.choice_3, variable=choice_var, value="3", font=("Arial", 30)).pack(anchor=tk.W, padx=20)
    tk.Radiobutton(root, text=current_choice4.choice_4, variable=choice_var, value="4", font=("Arial", 30)).pack(anchor=tk.W, padx=20)

    # 送信ボタンの作成
    submit_button = tk.Button(root, text="送信", command=submit_answer, font=("Arial", 30), width=10, height=2)
    submit_button.pack(pady=20)

    root.mainloop()

def submit_answer():
    selected_answer = choice_var.get()
    correct_answer = current_quiz.answer
    # explanation = current_quiz[6]
    explanation = "解説はないよ"

    # 解いた問題を記録し、次回以降表示されないようにする
    answered_quizzes.append(current_quiz)
    with open('gui/answered_quizzes.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(answered_quizzes)

    # クイズリストから解いた問題を削除
    quiz_list.remove(current_quiz)

    # 正解発表用のスクリプトを非同期で実行
    subprocess.Popen(['python', 'gui/result.py', selected_answer, correct_answer, explanation])
    root.destroy()

def show_no_quiz_message():
    no_quiz_root = tk.Tk()
    no_quiz_root.title("クイズ終了")
    no_quiz_root.attributes('-fullscreen', True)

    no_quiz_label = tk.Label(no_quiz_root, text="もうクイズがありません", font=("Arial", 50), bg="red", fg="white")
    no_quiz_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def back_to_title():
        no_quiz_root.destroy()
        subprocess.Popen(['python', 'gui/title.py'])

    title_button = tk.Button(no_quiz_root, text="タイトルに戻る", command=back_to_title, font=("Arial", 14))
    title_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    no_quiz_root.mainloop()

# クイズデータを読み込む
# load_quiz_data('gui/quiz.csv')
load_quiz_data(3)

# クイズウィンドウを作成
create_quiz_window()
