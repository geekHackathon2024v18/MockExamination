import tkinter as tk
from data.database.sql_alchemy_control import SqlAlchemyControl

def create_window():
    root = tk.Tk()
    root.title("pdf")
    root.attributes('-fullscreen', True)
    db = SqlAlchemyControl()
    
    # 全ての科目を取得
    subjects = db.read.subject()

    label = tk.Label(root, text="読み込み", font=("Arial", 70), bg="white", fg="black")
    label.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
    
    # 科目のリストを表示するリストボックスを追加
    subject_listbox = tk.Listbox(root, font=("Arial", 14))
    subject_listbox.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
    
    for subject in subjects:
        subject_listbox.insert(tk.END, subject)

    def back_to_title():
        root.destroy()
        from gui.title import open_title_window
        open_title_window(None)

    title_button = tk.Button(root, text="タイトルに戻る", command=back_to_title, font=("Arial", 14))
    title_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    root.mainloop()

if __name__ == "__main__":
    create_window()
