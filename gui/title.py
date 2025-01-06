import tkinter as tk
from importlib import import_module

def open_window(module_name, current_root):
    current_root.destroy()
    module = import_module(module_name)
    module.create_window()

def open_title_window(prev_root):
    if prev_root:
        prev_root.destroy()

    root = tk.Tk()
    root.title("home")
    root.attributes('-fullscreen', True)

    label = tk.Label(root, text="ホーム", font=("Arial", 70), bg="white", fg="black")
    label.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

    btn1 = tk.Button(root, text="pdf読み込み", font=("Arial", 30), bg="white", fg="black", command=lambda: open_window('pdf', root))
    btn1.place(relx=0.2, rely=0.65, anchor=tk.CENTER)

    btn2 = tk.Button(root, text="問題", font=("Arial", 30), bg="white", fg="black", command=lambda: open_window('question', root))
    btn2.place(relx=0.4, rely=0.65, anchor=tk.CENTER)

    btn3 = tk.Button(root, text="復習", font=("Arial", 30), bg="white", fg="black", command=lambda: open_window('review', root))
    btn3.place(relx=0.6, rely=0.65, anchor=tk.CENTER)

    btn4 = tk.Button(root, text="終了", font=("Arial", 30), bg="white", fg="black", command=root.destroy)
    btn4.place(relx=0.8, rely=0.65, anchor=tk.CENTER)

    root.mainloop()
