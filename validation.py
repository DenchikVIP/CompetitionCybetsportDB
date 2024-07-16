import re
import tkinter.messagebox as t

global key


def digit(name, type):
    if type == "1" and len(name) == 1:
        result = re.match(r"^\d*$", name) is not None
        if not result:
            t.showerror("Ошибка ввода", "В данное поле можно вводить только цифры")
        return result
    else:
        return re.match(r"^.*$", name) is not None


def word(name):
    result = re.match(
        r"[йцукенгшщзхъфывапролджэячсмитьбюёqwertyuiopasdfghjklzxcvbnmЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁQWERTYUIOPASDFGHJKLZXCVBNM -]*$",
        name) is not None
    if not result:
        t.showerror("Ошибка ввода",
                    "В данное поле можно вводить только буквы кириллицы и латиницы, а также пробел и дефис")
    return result


def phone(event):
    change = event.char
    if len(event.widget.get()) >= 19:
        event.widget.delete(18, "end")
    elif re.match(r"^[+]$", event.widget.get()) is not None:
        event.widget.delete(0, "end")
    elif re.match(r"^\d$", event.widget.get()) is not None:
        event.widget.delete(0, "end")
        event.widget.insert(0, "+" + change)
    elif re.match(r"^[+]\d\d$", event.widget.get()) is not None:
        event.widget.delete(2, "end")
        event.widget.insert(2, " (" + change)
    elif re.match(r"^[+]\d \(\d{4}$", event.widget.get()) is not None:
        event.widget.delete(7, "end")
        event.widget.insert(7, ") " + change)
    elif re.match(r"^[+]\d \(\d{3}\) \d{4}$", event.widget.get()) is not None:
        event.widget.delete(12, "end")
        event.widget.insert(12, "-" + change)
    elif re.match(r"^[+]\d \(\d{3}\) \d{3}-\d{3}$", event.widget.get()) is not None:
        event.widget.delete(15, "end")
        event.widget.insert(15, "-" + change)
    elif re.match(r"^[+]\d \(\d{3}\) \d{3}-\d{2}-$", event.widget.get()) is not None:
        event.widget.delete(15, "end")
    elif re.match(r"^[+]\d \(\d{3}\) \d{3}-$", event.widget.get()) is not None:
        event.widget.delete(12, "end")
    elif re.match(r"^[+]\d \(\d{3}\) $", event.widget.get()) is not None:
        event.widget.delete(7, "end")
    elif re.match(r"^[+]\d \(\d{3}\)$", event.widget.get()) is not None:
        event.widget.delete(7, "end")
    elif re.match(r"^[+]\d \($", event.widget.get()) is not None:
        event.widget.delete(2, "end")
    elif re.match(r"^[+]\d $", event.widget.get()) is not None:
        event.widget.delete(2, "end")


def date(event):
    change = event.char
    if len(event.widget.get()) >= 11:
        event.widget.delete(10, "end")
    elif re.match(r"^\d{5}$", event.widget.get()) is not None:
        event.widget.delete(4, "end")
        event.widget.insert(4, "-" + change)
    elif re.match(r"^\d{4}-$", event.widget.get()) is not None:
        event.widget.delete(4, "end")
    elif re.match(r"^\d{4}-\d{3}$", event.widget.get()) is not None:
        event.widget.delete(7, "end")
        event.widget.insert(7, "-" + change)
    elif re.match(r"^\d{4}-\d{2}-$", event.widget.get()) is not None:
        event.widget.delete(7, "end")
