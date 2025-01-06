import tkinter as tk
import csv
from importlib import import_module

def load_answered_quizzes(filename):
    answered_quizzes = []
    try:
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            answered_quizzes = list(reader)
    except FileNotFoundError:
        print("解いた問題のファイルが見つかりません")
    return answered_quizzes

def reset_answered_quizzes(root):
    answered_quizzes = load_answered_quizzes('gui/answered_quizzes.csv')
    
    with open('gui/quiz.csv', 'a', newline='', encoding='utf-8') as quizfile:
        writer = csv.writer(quizfile)
        writer.writerows(answered_quizzes)
    
    with open('gui/answered_quizzes.csv', 'w', newline='', encoding='utf-8') as f:
        pass
    
    reset_message = tk.Label(root, text="解いた問題をリセットしました", font=("Arial", 16), bg="white", fg="black")
    reset_message.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

def create_window():
    root = tk.Tk()
    root.title("復習")
    root.attributes('-fullscreen', True)

    answered_quizzes = load_answered_quizzes('gui/answered_quizzes.csv')

    if not answered_quizzes:
        no_quizzes_label = tk.Label(root, text="解いた問題がありません", font=("Arial", 50), bg="red", fg="white")
        no_quizzes_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    else:
        for i, quiz in enumerate(answered_quizzes):
            question_label = tk.Label(root, text=f"問題 {i+1}: {quiz[0]}", font=("Arial", 16))
            question_label.pack(pady=10)
            for j in range(1, 5):
                choice_label = tk.Label(root, text=f"選択肢 {j}: {quiz[j]}", font=("Arial", 14))
                choice_label.pack(pady=5)

    def open_title():
        root.destroy()
        from gui.title import open_title_window
        open_title_window(None)

    title_button = tk.Button(root, text="タイトルに戻る", command=open_title, font=("Arial", 14))
    title_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

    reset_button = tk.Button(root, text="問題をリセットする", command=lambda: reset_answered_quizzes(root), font=("Arial", 14), bg="white", fg="black")
    reset_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    root.mainloop()

if __name__ == "__main__":
    create_window()
