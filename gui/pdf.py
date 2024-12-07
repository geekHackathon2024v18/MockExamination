import tkinter as tk
import subprocess


# tkオブジェクトの作成
root = tk.Tk()
root.title("pdf")  # ウィンドウのタイトルを設定
root.attributes('-fullscreen', True)  # 全画面表示を有効にする

def open_title():
    subprocess.Popen(['python', 'gui/title.py'])
    root.withdraw()  # 現在のウィンドウを閉じる

# ウィジェットの配置や、イベント処理などを記述
label = tk.Label(root, text="読み込み", font=("Arial", 70), bg="white", fg="black")
label.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

title_button = tk.Button(root, text="タイトルに戻る", command=open_title, font=("Arial", 14))
title_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

# メインループの実行
root.mainloop()