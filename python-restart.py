from tkinter import *
#원래는 import 안쓰고 tkinter.Tk() 같이 써야함

root = Tk()
root.title("와! GUI!")
root.geometry("320x240")
#창의 속성 지정

btn1=Button(root,activebackground="#16AC81", text="와! 꺼무위키색!")
btn2=Button(root,activebackground="#1DA1F2", text="누르면 트위터 색!")
label1=Label(root, text="라벨?",anchor="s", fg="blue", bitmap="error")
label2=Label(root,text="경고!",anchor="center", width="1",height="1", relief="flat")

label1.pack()
label2.pack()
btn1.pack()
btn2.pack()

root.mainloop()