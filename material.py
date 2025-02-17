import tkinter as t
import tkinter.ttk as ttk
import connect as con
import validation as v

global number
global very_massive
global main_frame
global secondary_frame
global center_frame
global type_of_view
global uid_var
global focus


def create_window():
    global type_of_view
    global main_frame
    global secondary_frame
    global center_frame
    global very_massive
    global number
    type_of_view = True
    very_massive = con.extract("Material")
    number = 0
    main_window = t.Tk()
    main_window.title("Карточка материалов")
    main_window.resizable(width=False, height=False)

    def create_frame():
        global main_frame
        main_frame = t.Frame(
            main_window
        )
        main_frame.grid(row=2)

        global secondary_frame
        secondary_frame = t.Frame(
            main_frame
        )
        secondary_frame.grid(row=3, column=2)

        global center_frame
        center_frame = t.Frame(
            main_frame,
            padx=5,
            pady=5,
        )
        center_frame.grid(row=2, column=2)

    def kill_view():
        global main_frame
        global type_of_view
        main_frame.destroy()
        if type_of_view:
            show_tree()
            type_of_view = False
        else:
            show_form()
            type_of_view = True

    def show_tree():
        create_frame()
        tree = ttk.Treeview(
            center_frame,
            columns=("UID", "Name", "Cost", "Unit"),
            show="headings",
            selectmode="browse",
        )
        tree.grid(row=3)
        tree.heading("UID", text="Уникальный идентификатор")
        tree.heading("Name", text="Название материала")
        tree.heading("Cost", text="Стоимость материала за единицу измерения")
        tree.heading("Unit", text="Единица измерения")

        def update_tree():
            global very_massive
            tree.delete(*tree.get_children())
            for var in very_massive:
                tree.insert(parent="", index="end", values=var)

        update_tree()
        explanation = t.Label(center_frame, text="Выбранная строка")
        explanation.grid(row=1)
        entry_frame = t.Frame(center_frame)
        entry_frame.grid(row=2)
        uid_entry = t.Entry(entry_frame)
        uid_entry.grid(column=1, row=1)
        name_entry = t.Entry(entry_frame)
        name_entry.grid(column=2, row=1)
        cost_entry = t.Entry(entry_frame)
        cost_entry.grid(column=3, row=1)
        unit_entry = t.Entry(entry_frame)
        unit_entry.grid(column=4, row=1)

        def row_pick(event):
            # Какой-то баг я не понимаю
            tree.item(tree.selection()[0])
            # Без /\этой/\ строки ничего не работает
            uid_entry.delete(0, t.END)
            uid_entry.insert(0, tree.item(tree.selection()[0])["values"][0])
            cost_entry.delete(0, t.END)
            cost_entry.insert(0, tree.item(tree.selection()[0])["values"][2])
            name_entry.delete(0, t.END)
            name_entry.insert(0, tree.item(tree.selection()[0])["values"][1])
            unit_entry.delete(0, t.END)
            unit_entry.insert(0, tree.item(tree.selection()[0])["values"][3])

        tree.bind("<<TreeviewSelect>>", row_pick)

        def change_info():
            con.change_mat((uid_entry.get(), name_entry.get(), cost_entry.get(), unit_entry.get()))
            global very_massive
            very_massive = con.extract("Material")
            update_tree()

        def add_info():
            con.create_mat((uid_entry.get(), name_entry.get(), cost_entry.get(), unit_entry.get()))
            global very_massive
            very_massive = con.extract("Material")
            update_tree()

        def delete_info():
            con.delete("Material", uid_entry.get())
            global very_massive
            very_massive = con.extract("Material")
            update_tree()

        add = t.Button(
            secondary_frame,
            command=add_info
        )
        add.configure(text="Добавить новую запись")
        add.grid(row=1, column=2)

        delete = t.Button(
            secondary_frame,
            command=delete_info
        )
        delete.configure(text="Удалить выбранную запись")
        delete.grid(row=1, column=3)

        change = t.Button(
            secondary_frame,
            command=change_info
        )
        change.configure(text="Сохранить выбранную запись")
        change.grid(row=1, column=1)

    create_frame()

    switch = t.Button(
        main_window,
        command=kill_view
    )
    switch.configure(text="Сменить вид отображения")
    switch.grid(row=1, sticky="nw")

    def show_form():
        global very_massive
        global number
        create_frame()
        uid_label = t.Label(
            center_frame,
        )
        uid_label.grid(row=1, column=1, pady=5)
        uid_label.configure(text="Уникальный идентификатор")

        name_label = t.Label(
            center_frame,
        )
        name_label.grid(row=2, column=1, pady=5)
        name_label.configure(text="Название материала")

        cost_label = t.Label(
            center_frame,
        )
        cost_label.grid(row=3, column=1, pady=5)
        cost_label.configure(text="Стоимость материала")

        unit_label = t.Label(
            center_frame,
        )
        unit_label.grid(row=4, column=1, pady=5)
        unit_label.configure(text="Единица измерения")

        check_digit = (main_window.register(v.digit), "%S", "%d")
        check_word = (main_window.register(v.word), "%P")

        uid_entry = t.Entry(
            center_frame,
            validate="key",
            validatecommand=check_digit
        )
        uid_entry.grid(row=1, column=2, pady=5)
        uid_entry.insert(0, very_massive[number][0])

        name_entry = t.Entry(
            center_frame,
            validate="key",
            validatecommand=check_word
        )
        name_entry.grid(row=2, column=2, pady=5)
        name_entry.insert(0, very_massive[number][1])

        cost_entry = t.Entry(
            center_frame,
            validate="key",
            validatecommand=check_digit
        )
        cost_entry.grid(row=3, column=2, pady=5)
        cost_entry.insert(0, very_massive[number][2])

        unit_entry = t.Entry(
            center_frame,
        )
        unit_entry.grid(row=4, column=2, pady=5)
        unit_entry.insert(0, very_massive[number][3])

        def next_page():
            global number
            number += 1
            if number >= len(very_massive):
                number = 0
            unit_entry.delete(0, t.END)
            unit_entry.insert(0, very_massive[number][3])
            cost_entry.delete(0, t.END)
            cost_entry.insert(0, very_massive[number][2])
            name_entry.delete(0, t.END)
            name_entry.insert(0, very_massive[number][1])
            uid_entry.delete(0, t.END)
            uid_entry.insert(0, very_massive[number][0])

        def prev_page():
            global number
            number = number - 1
            if number < 0:
                number = len(very_massive) - 1
            unit_entry.delete(0, t.END)
            unit_entry.insert(0, very_massive[number][3])
            cost_entry.delete(0, t.END)
            cost_entry.insert(0, very_massive[number][2])
            name_entry.delete(0, t.END)
            name_entry.insert(0, very_massive[number][1])
            uid_entry.delete(0, t.END)
            uid_entry.insert(0, very_massive[number][0])

        before_bt = t.Button(
            main_frame,
            command=prev_page
        )
        before_bt.configure(text="<")
        before_bt.grid(row=3, column=1)

        after_bt = t.Button(
            main_frame,
            command=next_page
        )
        after_bt.configure(text=">")
        after_bt.grid(row=3, column=3)

        def change_info():
            con.change_mat((uid_entry.get(), name_entry.get(), cost_entry.get(), unit_entry.get()))
            global very_massive
            very_massive = con.extract("Material")
            global number
            number = 0
            next_page()
            prev_page()

        def add_info():
            con.create_mat((uid_entry.get(), name_entry.get(), cost_entry.get(), unit_entry.get()))
            global very_massive
            very_massive = con.extract("Material")
            global number
            number = 0
            next_page()
            prev_page()

        def delete_info():
            con.delete("Material", uid_entry.get())
            global very_massive
            very_massive = con.extract("Material")
            global number
            number = 0
            next_page()
            prev_page()

        add = t.Button(
            secondary_frame,
            command=add_info
        )
        add.configure(text="Добавить новую запись")
        add.grid(row=1, column=2)

        delete = t.Button(
            secondary_frame,
            command=delete_info
        )
        delete.configure(text="Удалить запись")
        delete.grid(row=1, column=3)

        change = t.Button(
            secondary_frame,
            command=change_info
        )
        change.configure(text="Сохранить запись")
        change.grid(row=1, column=1)

    show_form()
    t.mainloop()
