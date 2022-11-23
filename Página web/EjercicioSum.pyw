from tkinter import Tk,Label,Button,Entry

vent= Tk()
vent.config(bg="#BAEFFF")
vent.title=("Primer prueba")
vent.geometry("400x200")


def suma(): 
    
    n1 = text1.get()
    n2 = text2.get()
    r = float(n1)+float(n2)
    text3.delete(0,'end')
    text3.insert(0,r)


lbl1 = Label(vent, text="primer numero", bg="cyan")
lbl1.place(x=10, y=10, width=100, height=30)

text1= Entry(vent, bg="pink")
text1.place(x=120, y=10, width=100, height=30)


lbl2 = Label(vent, text="segundo  numero", bg="cyan")
lbl2.place(x =10 , y=50, width=100, height=30)

text2=Entry(vent, bg="pink")
text2.place(x =120 , y=50, width=100, height=30)

bt1=Button(vent, text='sumar', command=suma)
bt1.place(x=230, y= 50, width=100, height=30)





lbl3 = Label(vent, text="Resultado", bg="cyan")
lbl3.place(x=10, y=120, width=100, height=30)
text3=Entry(vent, bg="pink")
text3.place(x=120, y=120, width=100, height=30)













vent.mainloop()
