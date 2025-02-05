import tkinter as tk
import csv
import random
from gui.result import create_result_window

quiz_list = []
answered_quizzes = []
choice_var = None
current_quiz = None

def load_quiz_data(filename):
    global quiz_list, answered_quizzes
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        quiz_list = list(reader)

    try:
        with open('gui/answered_quizzes.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            answered_quizzes = list(reader)
    except FileNotFoundError:
        answered_quizzes = []

    quiz_list = [quiz for quiz in quiz_list if quiz not in answered_quizzes]

def create_window():
    global choice_var, current_quiz

    root = tk.Tk()
    root.title("4択クイズ")
    root.attributes('-fullscreen', True)

    if len(quiz_list) == 0:
        show_no_quiz_message(root)
        return

    current_quiz = random.choice(quiz_list)
    
    question_label = tk.Label(root, text=current_quiz[0], font=("Arial", 30))
    question_label.pack(pady=20)
    
    choice_var = tk.StringVar()
    choice_var.set(None)
    
    for i in range(1, 5):
        tk.Radiobutton(root, text=current_quiz[i], variable=choice_var, value=current_quiz[i], font=("Arial", 30)).pack(anchor=tk.W, padx=20)
    
    submit_button = tk.Button(root, text="送信", command=lambda: submit_answer(root), font=("Arial", 30), width=10, height=2)
    submit_button.pack(pady=20)
    
    root.mainloop()

def submit_answer(root):
    selected_answer = choice_var.get()
    correct_answer = current_quiz[5]
    explanation = current_quiz[6]

    answered_quizzes.append(current_quiz)
    with open('gui/answered_quizzes.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(answered_quizzes)
    
    quiz_list.remove(current_quiz)

    create_result_window(selected_answer, correct_answer, explanation, root)  # 結果画面を表示

def show_no_quiz_message(root):
    no_quiz_root = tk.Toplevel(root)
    no_quiz_root.title("クイズ終了")
    no_quiz_root.attributes('-fullscreen', True)

    no_quiz_label = tk.Label(no_quiz_root, text="もうクイズがありません", font=("Arial", 50), bg="red", fg="white")
    no_quiz_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def back_to_title():
        no_quiz_root.destroy()
        from gui.title import open_title_window
        open_title_window(None)

    title_button = tk.Button(no_quiz_root, text="タイトルに戻る", command=back_to_title, font=("Arial", 14))
    title_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    no_quiz_root.mainloop()

load_quiz_data('quiz.csv')

if __name__ == "__main__":
    create_window()
