import tkinter as tk
from gui.title import open_title_window

def open_main_window():
    root = tk.Tk()
    root.title("home")  # ウィンドウのタイトルを設定
    root.attributes('-fullscreen', True)  # 全画面表示を有効にする

    label = tk.Label(root, text="準備はいい？", font=("Arial", 70), bg="white", fg="black")
    label.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

    btn1 = tk.Button(root, text="勉強を始めよう！ここを押してね！", font=("Arial", 30), bg="white", fg="black", command=lambda: open_title_window(root))
    btn1.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

    # メインループの実行
    root.mainloop()

if __name__ == "__main__":
    open_main_window()
