import tkinter as tk

def create_result_window(answer, correct_answer, explanation, root):
    for widget in root.winfo_children():
        widget.destroy()

    if answer == correct_answer:
        result_text = f"正解です！\n\n{explanation}"
    else:
        result_text = f"不正解です。\n\n正解は {correct_answer} です。\n\n{explanation}"

    result_label = tk.Label(root, text=result_text, font=("Arial", 30), bg="blue", fg="white")
    result_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def open_title():
        root.destroy()
        from gui.title import open_title_window
        open_title_window(None)

    def open_review():
        root.destroy()
        from gui.review import create_window
        create_window()

    def continue_quiz():
        root.destroy()
        from gui.question import create_window
        create_window()

    title_button = tk.Button(root, text="タイトルに戻る", command=open_title, font=("Arial", 14))
    title_button.place(relx=0.2, rely=0.7, anchor=tk.CENTER)

    review_button = tk.Button(root, text="復習する", command=open_review, font=("Arial", 14))
    review_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    continue_button = tk.Button(root, text="続けて解く", command=continue_quiz, font=("Arial", 14))
    continue_button.place(relx=0.8, rely=0.7, anchor=tk.CENTER)

if __name__ == "__main__":
    create_result_window('', '', '', tk.Tk())
