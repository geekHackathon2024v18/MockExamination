import tkinter as tk

def create_window():
    root = tk.Tk()
    root.title("pdf")
    root.attributes('-fullscreen', True)

    label = tk.Label(root, text="読み込み", font=("Arial", 70), bg="white", fg="black")
    label.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

    def back_to_title():
        root.destroy()
        from gui.title import open_title_window
        open_title_window(None)

    title_button = tk.Button(root, text="タイトルに戻る", command=back_to_title, font=("Arial", 14))
    title_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    root.mainloop()

if __name__ == "__main__":
    create_window()
