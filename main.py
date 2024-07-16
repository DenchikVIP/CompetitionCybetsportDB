from tkinter import *
import client as cl
import worker as wrkr
import work as wrk
import material as mat
import equipment as eq
import order as ord

# def create():
window = Tk()
window.title("Выбор карточки")
frame = Frame(
    window
)
frame.grid(row=2)
client = Button(
    frame,
    text="Карточка клиента",
    font=25,
    command=cl.create_window,
    height=1,
    width=30
)
client.grid(row=1)
material = Button(
    frame,
    text="Карточка материалов",
    font=25,
    command=mat.create_window,
    height=1,
    width=30
)
material.grid(row=3)
equipment = Button(
    frame,
    text="Карточка инвентаря",
    font=25,
    command=eq.create_window,
    height=1,
    width=30
)
equipment.grid(row=4)
work = Button(
    frame,
    text="Карточка услуг",
    font=25,
    command=wrk.create_window,
    height=1,
    width=30
)
work.grid(row=5)
worker = Button(
    frame,
    text="Карточка рабочих",
    font=25,
    command=wrkr.create_window,
    height=1,
    width=30
)
worker.grid(row=2)
order = Button(
    frame,
    text="Карточка заказов",
    font=25,
    command=ord.create_window,
    height=1,
    width=30
)
order.grid(row=6)
title = Label(
    window,
    text="Выберите карточку",
    foreground="Blue",
    font=60
)
title.grid(row=1)
mainloop()
