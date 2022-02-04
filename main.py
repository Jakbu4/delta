from tkinter import *
from tkinter import font

root = Tk()
root.resizable(width=None, height=None)
root.title("delta\u00b2")

v = Canvas(root, width=540, height=700).pack()

x2 = Entry(v, width=5, font="Helvetica 20 bold")
x2.place(x=70, y=30)

Label(v, text="x\u00b2 + ", font="Helvetica 20 bold", fg='#444444').place(x=150, y=30)

x1 = Entry(v, width=5, font="Helvetica 20 bold")
x1.place(x=210, y=30)
Label(v, text="x + ", font="Helvetica 20 bold", fg='#444444').place(x=290, y=30)

x0 = Entry(v, width=5, font="Helvetica 20 bold")
x0.place(x=340, y=30)
Label(v, text=" = 0", font="Helvetica 20 bold", fg='#444444').place(x=420, y=30)


def delta():
    a = float(x2.get())
    b = float(x1.get())
    c = float(x0.get())

    dt = (b**2) - (4*a*c)
    p = round(((-1*b)/(2*a)),2)
    q = round(((-1*dt)/(4*a)),2)

    dt_l = Label(v, text=f"\u0394 = {dt}", font="Helvetica 20 bold").place(x=215, y=190)
    p_l = Label(v, text=f"p = {p}", font="Helvetica 15 bold").place(x=140, y=360)
    q_l = Label(v, text=f"q = {q}", font="Helvetica 15 bold").place(x=320, y=360)
    if p>0:
        p_k = Label(v, text=f"Postać kanoniczna: f(x) = {a}(x-{p})\u00b2+({q})", font="Helvetica 15 bold").place(x=50, y=420)
    else:
         p_k = Label(v, text=f"Postać kanoniczna: f(x) = {a}(x+{abs(p)})\u00b2+({q})", font="Helvetica 15 bold").place(x=60, y=420)
    if dt > 0:
        mz1 = round((((-1)*b) + (dt**(1/2))) / (2*a), 2)
        mz2 = round((((-1)*b) - (dt**(1/2))) / (2*a), 2)
        mz1_l = Label(v, text=f"x\u2081 = {mz1}", font="Helvetica 15 bold").place(x=220, y=260)
        mz2_l = Label(v, text=f"x\u2082 = {mz2}", font="Helvetica 15 bold").place(x=220, y=310)
        return dt_l, mz1_l, mz2_l, p_l, q_l, p_k
    elif dt == 0:
        mz1 = ((-1)*b) / (2*a)
        mz1_l = Label(v, text=f"x1 = {mz1}", font="Helvetica 15 bold").place(x=220, y=260)
        return dt_l, mz1_l, p_l, q_l, p_k
    elif dt < 0:
        mz0_l = Label(v, text="brak miejsc zerowych", font="Helvetica 15 bold").place(x=165, y=280)
        return dt_l, mz0_l, p_l, q_l, p_k

    

calc = Button(v, text="\u0394",command=delta, font="Helvetica 20 bold", padx=30, activebackground='#3E4149').place(x=220, y=100)

root.mainloop()
