from tkinter import *
from tkinter.font import Font

root=Tk()
font=Font(size=15)
e1=Entry(root,bg='black',fg='white',width=25)
e1['font']=font
e1.grid(row=0,columnspan=4)
root.title('calculator')
def angka(nilai):
    sebelum=e1.get()
    e1.delete(0,END)
    e1.insert(0,str(sebelum)+str(nilai))
def reset():
    e1.delete(0,END)
button7=Button(root,text=7,padx=25,pady=20,command=lambda:angka(7))
button8=Button(root,text=8,padx=25,pady=20,command=lambda:angka(8))
button9=Button(root,text=9,padx=25,pady=20,command=lambda:angka(9))
button4=Button(root,text=4,padx=25,pady=20,command=lambda:angka(4))
button5=Button(root,text=5,padx=25,pady=20,command=lambda:angka(5))
button6=Button(root,text=6,padx=25,pady=20,command=lambda:angka(6))
button1=Button(root,text=1,padx=25,pady=20,command=lambda:angka(1))
button2=Button(root,text=2,padx=25,pady=20,command=lambda:angka(2))
button3=Button(root,text=3,padx=25,pady=20,command=lambda:angka(3))
button0=Button(root,text=0,padx=25,pady=20,command=lambda:angka(0))
buttonminus=Button(root,text='+/-',padx=25,pady=20,command=lambda:angka('-'))
decimal=Button(root,text='.',pady=20,padx=25,command=lambda:angka('.'))
resett=Button(root,text='del',padx=25,pady=20,command=reset)
def plus():
    global status
    global initial
    status='plus'
    initial=float(e1.get())
    e1.delete(0,END)
def minus():
    global status
    global initial
    status='minus'
    initial=float(e1.get())
    e1.delete(0,END)
def multipy():
    global status
    global initial
    status='multipy'
    initial=float(e1.get())
    e1.delete(0,END)

def devided():
    global status
    global initial
    initial=float(e1.get())
    status='devided'
    e1.delete(0,END)
def equal():
    if status=='devided':
        final=float(e1.get())
        e1.delete(0,END)
        try:
            result=initial/final
            return e1.insert(0,result)
        except ZeroDivisionError:
            return e1.insert(0,'Can\'t Divided with Zero')
    elif status=='multipy':
        final=float(e1.get())
        e1.delete(0,END)
        result=initial*final
        return e1.insert(0,result)
    elif status=='plus':
        final=float(e1.get())
        e1.delete(0,END)
        result=initial+final
        return e1.insert(0,result)
    elif status=='minus':
        final=float(e1.get())
        e1.delete(0,END)
        result=initial-final
        return e1.insert(0,result)

plu=Button(root,text='+',padx=25,pady=20,command=plus).grid(row=1,column=3)
minu=Button(root,text='-',padx=25,pady=20,command=minus).grid(row=2,column=3)
devi=Button(root,text=':',padx=25,pady=20,command=devided).grid(row=3,column=3)
multiply=Button(root,text='x',padx=25,pady=20,command=multipy).grid(row=4,column=3)
equals=Button(root,text='=',padx=25,pady=20,command=equal).grid(row=4,column=2)

button7.grid(row=1,column=0,pady=2)
button8.grid(row=1,column=1,pady=2)
button9.grid(row=1,column=2,pady=2)
button4.grid(row=2,column=0,pady=2)
button5.grid(row=2,column=1,pady=2)
button6.grid(row=2,column=2,pady=2)
button1.grid(row=3,column=0,pady=2)
button2.grid(row=3,column=1,pady=2)
button3.grid(row=3,column=2,pady=2)
button0.grid(row=4,column=1,pady=2)
buttonminus.grid(row=4,column=0,pady=2)
decimal.grid(row=5,column=2,pady=2)
resett.grid(row=5,column=3,pady=2)
root.mainloop()