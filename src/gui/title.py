import tkinter as tk
import subprocess

# tkオブジェクトの作成
root = tk.Tk()
root.title("home")  # ウィンドウのタイトルを設定
root.attributes('-fullscreen', True)  # 全画面表示を有効にする

def open_question():
    # 少し時間を置いてから次のウィンドウを開く
    subprocess.Popen(['python', 'src/gui/question.py'])
    root.destroy()

def open_review():
    # 少し時間を置いてから次のウィンドウを開く
    subprocess.Popen(['python', 'src/gui/review.py'])
    root.destroy()

def open_pdf():
    # 少し時間を置いてから次のウィンドウを開く
    subprocess.Popen(['python', 'src/gui/pdf.py'])
    root.destroy()

# ウィジェットの配置
label = tk.Label(root, text="ホーム", font=("Arial", 70), bg="white", fg="black")
label.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

btn1 = tk.Button(root, text="pdf読み込み", font=("Arial", 30), bg="white", fg="black", command=open_pdf)
btn1.place(relx=0.2, rely=0.65, anchor=tk.CENTER)

btn2 = tk.Button(root, text="問題", font=("Arial", 30), bg="white", fg="black", command=open_question)
btn2.place(relx=0.4, rely=0.65, anchor=tk.CENTER)

btn3 = tk.Button(root, text="復習", font=("Arial", 30), bg="white", fg="black", command=open_review)
btn3.place(relx=0.6, rely=0.65, anchor=tk.CENTER)

btn4 = tk.Button(root, text="終了", font=("Arial", 30), bg="white", fg="black", command=root.destroy)
btn4.place(relx=0.8, rely=0.65, anchor=tk.CENTER)

# メインループの実行
root.mainloop()
