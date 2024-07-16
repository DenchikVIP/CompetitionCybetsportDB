from tkinter import *
import main as Mn


def func(name):  # СЗъделай валидацию!!!
    if True:
        return True
    else:
        return False


def next_page():
    Mn.create(2)
    login.destroy()


login = Tk()
login.title("Вход")
frame = Frame(
    login,
    padx=10,
    pady=10,
)
frame.pack(expand=True)
enter1 = Entry(
    frame,
    font=10,
    validate="key",
    validatecommand=(login.register(func), "%P")  # СЗъделай валидацию!!!
)
enter1.insert(1, "1234567890")
enter1.grid(row=2)
explanation1 = Label(
    frame,
    text="Введите свой Uid",
    font=16
)
explanation1.grid(row=1)
enter2 = Entry(
    frame,
    font=10
)
enter2.insert(1, "+7 (999) 999-99-99")
enter2.grid(row=4)
explanation2 = Label(
    frame,
    text="Введите свой номер телефона",
    font=16  # СЗъделай валидацию!!!
)
explanation2.grid(row=3)
buter = Button(
    frame,
    text="Жмяк",
    font=25,
    command=next_page
)
buter.grid(row=6)
mainloop()
