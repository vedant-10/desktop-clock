from tkinter import *
from datetime import datetime
from time import strftime

w=Tk()
w.geometry('350x150+620+300')
w.minsize(270,150)
w.overrideredirect(False)
w.wm_attributes('-transparentcolor','#FFFFFF')
w.config(bg='#FFFFFF',bd=0,highlightthickness=0)
a=datetime.today().strftime('%a')
b=(a.upper())
d=datetime.today().strftime('%d %B %Y')
e=(d.upper())
f1=Frame(w,width=350, height=150,bg='#FFFFFF')
f1.pack(expand=False)
#Mechenism
def time():
    a=strftime('%H : %M')  #%H   %M   %S
    l1.config(text=a)
    l1.after(1000,time)

l1=Label(f1, font=('Noto Serif Toto',60),bg='#FFFFFF',foreground='#F0FFFF')
l1.place(anchor="center",relx=0.5,rely=0.3)
time()

l2=Label(f1, font=('Candara',20),bg='#FFFFFF',foreground='#F0FFFF')
l2.config(text=e)
l2.place(anchor="center",relx=0.4,rely=0.8)

l3=Label(f1, font=('Candara',20),bg='#FFFFFF',foreground='#F0FFFF')
l3.config(text=b)
l3.place(anchor="center",relx=0.8,rely=0.8)

w.mainloop()