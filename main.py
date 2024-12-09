import tkinter as tk
import subprocess

root = tk.Tk()
root.title("home")  # ウィンドウのタイトルを設定
root.attributes('-fullscreen', True)  # 全画面表示を有効にする

def open_title():
    # 少し時間を置いてから次のウィンドウを開く
    subprocess.Popen(['python', 'gui/title.py'])
    root.withdraw()  # 関数として呼び出す

label = tk.Label(root, text="準備はいい？", font=("Arial", 70), bg="white", fg="black")
label.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

btn1 = tk.Button(root, text="勉強を始めよう！ここを押してね！", font=("Arial", 30), bg="white", fg="black", command=open_title)
btn1.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

# メインループの実行
root.mainloop()
