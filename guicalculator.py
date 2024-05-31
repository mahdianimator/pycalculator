from tkinter import *
from tkinter import messagebox

a = Tk()
a.title("ماشین حساب")
a.geometry("400x400")

aval = True
dovom = True

def run():
    aval = float(ent.get())
    dovom = float(entnum2.get())
    lebgb.config(text= aval + dovom)
    lebmb.config(text= aval - dovom)
    lebzb.config(text= aval * dovom)
    lebtb.config(text= aval / dovom)

ent = Entry(a,font=("arial", 20))
ent.pack()

entnum2 = Entry(a,font=("arial", 20))
entnum2.pack()

btn = Button(a,font=("arial", 20), text="فعال کنید", command=run)
btn.pack()

lebg = Label(a, text="جمع : ", font=("arial", 20))
lebg.place(x=40, y=130)

lebm = Label(a, text="تفریق : ", font=("arial", 20))
lebm.place(x=40, y=180)

lebz = Label(a, text="ضرب : ", font=("arial", 20))
lebz.place(x=40, y=230)

lebt = Label(a, text="تقسیم : ", font=("arial", 20))
lebt.place(x=40, y=280)




lebgb = Label(a, font=("arial", 20))
lebgb.place(x=150, y=130)

lebmb = Label(a, font=("arial", 20))
lebmb.place(x=150, y=180)

lebzb = Label(a, font=("arial", 20))
lebzb.place(x=150, y=230)

lebtb = Label(a, font=("arial", 20))
lebtb.place(x=150, y=280)


a.mainloop()