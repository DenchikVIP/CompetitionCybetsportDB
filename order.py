import tkinter as t
import tkinter.ttk as ttk

import connect as con
import validation as v

global number
global very_massive
global foreign_keys
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
    global foreign_keys
    global number
    type_of_view = True
    very_massive = con.extract("Order")
    foreign_keys = con.foreign_keys()
    number = 0
    main_window = t.Tk()
    main_window.title("Карточка заказов")
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
        tree_frame = t.Canvas(center_frame)
        tree_frame.grid(row=3)
        tree = ttk.Treeview(
            tree_frame,
            columns=("OrderUID", "ClientUID", "WorkUID", "Worker1UID", "Worker2UID", "Material1UID",
                     "Material1count", "Material2UID", "Material2count", "Equipment1UID", "Equipment2UID", "Datestart",
                     "Datefinish"),
            show="headings",
            selectmode="browse",
        )
        tree.heading("OrderUID", text="Уникальный идентификатор заказа")
        tree.column(0,width=50)
        tree.heading("ClientUID", text="Уникальный идентификатор клиента")
        tree.column(1, width=50)
        tree.heading("WorkUID", text="Уникальный идентификатор услуги")
        tree.column(2, width=50)
        tree.heading("Worker1UID", text="Уникальный идентификатор рабочего №1")
        tree.column(3, width=50)
        tree.heading("Worker2UID", text="Уникальный идентификатор рабочего №2")
        tree.column(4, width=50)
        tree.heading("Material1UID", text="Уникальный идентификатор материала №1")
        tree.column(5, width=50)
        tree.heading("Material1count", text="Количество материала №1")
        tree.column(6, width=50)
        tree.heading("Material2UID", text="Уникальный идентификатор материала №2")
        tree.column(7, width=50)
        tree.heading("Material2count", text="Количество материала №2")
        tree.column(8, width=50)
        tree.heading("Equipment1UID", text="Уникальный идентификатор снаряжения №1")
        tree.column(9, width=50)
        tree.heading("Equipment2UID", text="Уникальный идентификатор снаряжения №2")
        tree.column(10, width=50)
        tree.heading("Datestart", text="Дата начала работы")
        tree.column(11, width=50)
        tree.heading("Datefinish", text="Дата конца работы")
        tree.column(12, width=50)
        tree.pack(anchor="center", expand=0)
        scrollbar = ttk.Scrollbar(tree_frame, orient="horizontal", command=tree.xview)
        #scrollbar.pack(anchor="s", fill=t.X)
        tree.configure(xscrollcommand=scrollbar.set(0, 0.2))

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
        order_uid_entry = t.Entry(entry_frame)
        order_uid_entry.grid(column=1, row=1)
        client_uid_var = t.StringVar(value=foreign_keys[0][0])
        client_uid_combo_box = ttk.Combobox(entry_frame, textvariable=client_uid_var, values=foreign_keys[0],
                                            state="readonly")
        client_uid_combo_box.grid(column=2, row=1)
        work_uid_var = t.StringVar(value=foreign_keys[1][0])
        work_uid_combo_box = ttk.Combobox(entry_frame, textvariable=work_uid_var, values=foreign_keys[1],
                                          state="readonly")
        work_uid_combo_box.grid(column=3, row=1)
        worker1_uid_var = t.StringVar(value=foreign_keys[2][0])
        worker1_uid_combo_box = ttk.Combobox(entry_frame, textvariable=worker1_uid_var, values=foreign_keys[2],
                                             state="readonly")
        worker1_uid_combo_box.grid(column=4, row=1)
        worker2_uid_var = t.StringVar(value=foreign_keys[2][0])
        worker2_uid_combo_box = ttk.Combobox(entry_frame, textvariable=worker2_uid_var, values=foreign_keys[2],
                                             state="readonly")
        worker2_uid_combo_box.grid(column=5, row=1)
        material1_uid_var = t.StringVar(value=foreign_keys[3][0])
        material1_uid_combo_box = ttk.Combobox(entry_frame, textvariable=material1_uid_var, values=foreign_keys[3],
                                               state="readonly")
        material1_uid_combo_box.grid(column=1, row=2)
        material1_count_entry = t.Entry(entry_frame)
        material1_count_entry.grid(column=2, row=2)
        material2_uid_var = t.StringVar(value=foreign_keys[3][0])
        material2_uid_combo_box = ttk.Combobox(entry_frame, textvariable=material2_uid_var, values=foreign_keys[3],
                                               state="readonly")
        material2_uid_combo_box.grid(column=3, row=2)
        material2_count_entry = t.Entry(entry_frame)
        material2_count_entry.grid(column=4, row=2)
        equipment1_uid_var = t.StringVar(value=foreign_keys[4][0])
        equipment1_uid_combo_box = ttk.Combobox(entry_frame, textvariable=equipment1_uid_var, values=foreign_keys[4],
                                                state="readonly")
        equipment1_uid_combo_box.grid(column=5, row=2)
        equipment2_uid_var = t.StringVar(value=foreign_keys[4][0])
        equipment2_uid_combo_box = ttk.Combobox(entry_frame, textvariable=equipment2_uid_var, values=foreign_keys[4],
                                                state="readonly")
        equipment2_uid_combo_box.grid(column=1, row=3)
        date_start_entry = t.Entry(entry_frame)
        date_start_entry.grid(column=2, row=3)
        date_finish_entry = t.Entry(entry_frame)
        date_finish_entry.grid(column=3, row=3)

        def row_pick(event):
            # Какой-то баг я не понимаю
            tree.item(tree.selection()[0])
            # Без /\этой/\ строки ничего не работает
            order_uid_entry.delete(0, t.END)
            order_uid_entry.insert(0, tree.item(tree.selection()[0])["values"][0])
            for var in range(len(foreign_keys[0])):
                if foreign_keys[0][var] == tree.item(tree.selection()[0])["values"][1]:
                    client_uid_combo_box.current(var)
            for var in range(len(foreign_keys[1])):
                if foreign_keys[1][var] == tree.item(tree.selection()[0])["values"][2]:
                    work_uid_combo_box.current(var)
            for var in range(len(foreign_keys[2])):
                if foreign_keys[2][var] == tree.item(tree.selection()[0])["values"][3]:
                    worker1_uid_combo_box.current(var)
            for var in range(len(foreign_keys[2])):
                if foreign_keys[2][var] == tree.item(tree.selection()[0])["values"][4]:
                    worker2_uid_combo_box.current(var)
            for var in range(len(foreign_keys[3])):
                if foreign_keys[3][var] == tree.item(tree.selection()[0])["values"][5]:
                    material1_uid_combo_box.current(var)
            material1_count_entry.delete(0, t.END)
            material1_count_entry.insert(0, tree.item(tree.selection()[0])["values"][6])
            for var in range(len(foreign_keys[3])):
                if foreign_keys[3][var] == tree.item(tree.selection()[0])["values"][7]:
                    material2_uid_combo_box.current(var)
            material2_count_entry.delete(0, t.END)
            material2_count_entry.insert(0, tree.item(tree.selection()[0])["values"][8])
            for var in range(len(foreign_keys[4])):
                if foreign_keys[4][var] == tree.item(tree.selection()[0])["values"][9]:
                    equipment1_uid_combo_box.current(var)
            for var in range(len(foreign_keys[4])):
                if foreign_keys[4][var] == tree.item(tree.selection()[0])["values"][10]:
                    equipment2_uid_combo_box.current(var)

            date_start_entry.delete(0, t.END)
            date_start_entry.insert(0, tree.item(tree.selection()[0])["values"][11])
            date_finish_entry.delete(0, t.END)
            date_finish_entry.insert(0, tree.item(tree.selection()[0])["values"][12])

        tree.bind("<<TreeviewSelect>>", row_pick)

        def change_info():
            con.change_ord((order_uid_entry.get(), client_uid_var.get(), work_uid_var.get(), worker1_uid_var.get(),
                            worker2_uid_var.get(), material1_uid_var.get(), material1_count_entry.get(),
                            material2_uid_var.get(), material2_count_entry.get(), equipment1_uid_var.get(),
                            equipment2_uid_var.get(), date_start_entry.get(), date_finish_entry.get()))
            global very_massive
            very_massive = con.extract("Order")
            update_tree()

        def add_info():
            con.create_ord((order_uid_entry.get(), client_uid_var.get(), work_uid_var.get(), worker1_uid_var.get(),
                            worker2_uid_var.get(), material1_uid_var.get(), material1_count_entry.get(),
                            material2_uid_var.get(), material2_count_entry.get(), equipment1_uid_var.get(),
                            equipment2_uid_var.get(), date_start_entry.get(), date_finish_entry.get()))
            global very_massive
            very_massive = con.extract("Order")
            update_tree()

        def delete_info():
            con.delete("Order", order_uid_entry.get())
            global very_massive
            very_massive = con.extract("Order")
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
        order_uid_label = t.Label(center_frame)
        order_uid_label.grid(row=1, column=1, pady=5)
        order_uid_label.configure(text="Уникальный идентификатор заказа")
        client_uid_label = t.Label(center_frame)
        client_uid_label.grid(row=2, column=1, pady=5)
        client_uid_label.configure(text="Уникальный идентификатор клиента")
        work_uid_label = t.Label(center_frame)
        work_uid_label.grid(row=3, column=1, pady=5)
        work_uid_label.configure(text="Уникальный идентификатор услуги")
        worker1_uid_label = t.Label(center_frame)
        worker1_uid_label.grid(row=4, column=1, pady=5)
        worker1_uid_label.configure(text="Уникальный идентификатор рабочего №1")
        worker2_uid_label = t.Label(center_frame)
        worker2_uid_label.grid(row=5, column=1, pady=5)
        worker2_uid_label.configure(text="Уникальный идентификатор рабочего №2")
        material1_uid_label = t.Label(center_frame)
        material1_uid_label.grid(row=6, column=1, pady=5)
        material1_uid_label.configure(text="Уникальный идентификатор материала №1")
        material1_count_label = t.Label(center_frame)
        material1_count_label.grid(row=7, column=1, pady=5)
        material1_count_label.configure(text="Количество материала №1")
        material2_uid_label = t.Label(center_frame)
        material2_uid_label.grid(row=8, column=1, pady=5)
        material2_uid_label.configure(text="Уникальный идентификатор материала №2")
        material2_count_label = t.Label(center_frame)
        material2_count_label.grid(row=9, column=1, pady=5)
        material2_count_label.configure(text="Количество материала №2")
        equipment1_uid_label = t.Label(center_frame)
        equipment1_uid_label.grid(row=10, column=1, pady=5)
        equipment1_uid_label.configure(text="Уникальный идентификатор инструмента №1")
        equipment2_uid_label = t.Label(center_frame)
        equipment2_uid_label.grid(row=11, column=1, pady=5)
        equipment2_uid_label.configure(text="Уникальный идентификатор инструмента №2")
        date_start_label = t.Label(center_frame)
        date_start_label.grid(row=12, column=1, pady=5)
        date_start_label.configure(text="Дата начала")
        date_finish_label = t.Label(center_frame)
        date_finish_label.grid(row=13, column=1, pady=5)
        date_finish_label.configure(text="Дата конца")

        check_digit = (main_window.register(v.digit), "%S", "%d")
        check_date = (main_window.register(v.digit), "%S", "%d")

        order_uid_entry = t.Entry(
            center_frame,
            validate="key",
            validatecommand=check_digit
        )
        order_uid_entry.grid(row=1, column=2, pady=5)
        order_uid_entry.insert(0, very_massive[number][0])

        client_uid_var = t.StringVar(value=foreign_keys[0][0])
        client_uid_combo_box = ttk.Combobox(
            center_frame,
            values=foreign_keys[0],
            textvariable=client_uid_var,
            state="readonly"
        )
        client_uid_combo_box.grid(row=2, column=2, pady=5)
        for var in range(len(foreign_keys[0])):
            if foreign_keys[0][var] == very_massive[number][1]:
                client_uid_combo_box.current(var)

        work_uid_var = t.StringVar(value=foreign_keys[1][0])
        work_uid_combo_box = ttk.Combobox(
            center_frame,
            values=foreign_keys[1],
            textvariable=work_uid_var,
            state="readonly"
        )
        work_uid_combo_box.grid(row=3, column=2, pady=5)
        for var in range(len(foreign_keys[1])):
            if foreign_keys[1][var] == very_massive[number][2]:
                work_uid_combo_box.current(var)

        worker1_uid_var = t.StringVar(value=foreign_keys[2][0])
        worker1_uid_combo_box = ttk.Combobox(
            center_frame,
            values=foreign_keys[2],
            textvariable=worker1_uid_var,
            state="readonly"
        )
        worker1_uid_combo_box.grid(row=4, column=2, pady=5)
        for var in range(len(foreign_keys[2])):
            if foreign_keys[2][var] == very_massive[number][3]:
                worker1_uid_combo_box.current(var)

        worker2_uid_var = t.StringVar(value=foreign_keys[2][0])
        worker2_uid_combo_box = ttk.Combobox(
            center_frame,
            values=foreign_keys[2],
            textvariable=worker2_uid_var,
            state="readonly"
        )
        worker2_uid_combo_box.grid(row=5, column=2, pady=5)
        for var in range(len(foreign_keys[2])):
            if foreign_keys[2][var] == very_massive[number][4]:
                worker2_uid_combo_box.current(var)

        material1_uid_var = t.StringVar(value=foreign_keys[3][0])
        material1_uid_combo_box = ttk.Combobox(
            center_frame,
            values=foreign_keys[3],
            textvariable=material1_uid_var,
            state="readonly"
        )
        material1_uid_combo_box.grid(row=6, column=2, pady=5)
        for var in range(len(foreign_keys[3])):
            if foreign_keys[3][var] == very_massive[number][5]:
                material1_uid_combo_box.current(var)

        material1_count_entry = t.Entry(
            center_frame,
            validate="key",
            validatecommand=check_digit
        )
        material1_count_entry.grid(row=7, column=2, pady=5)
        material1_count_entry.insert(0, very_massive[number][6])

        material2_uid_var = t.StringVar(value=foreign_keys[3][0])
        material2_uid_combo_box = ttk.Combobox(
            center_frame,
            values=foreign_keys[3],
            textvariable=material2_uid_var,
            state="readonly"
        )
        material2_uid_combo_box.grid(row=8, column=2, pady=5)
        for var in range(len(foreign_keys[3])):
            if foreign_keys[3][var] == very_massive[number][7]:
                material2_uid_combo_box.current(var)

        material2_count_entry = t.Entry(
            center_frame,
            validate="key",
            validatecommand=check_digit
        )
        material2_count_entry.grid(row=9, column=2, pady=5)
        material2_count_entry.insert(0, very_massive[number][8])

        equipment1_uid_var = t.StringVar(value=foreign_keys[4][0])
        equipment1_uid_combo_box = ttk.Combobox(
            center_frame,
            values=foreign_keys[4],
            textvariable=equipment1_uid_var,
            state="readonly"
        )
        equipment1_uid_combo_box.grid(row=10, column=2, pady=5)
        for var in range(len(foreign_keys[4])):
            if foreign_keys[4][var] == very_massive[number][9]:
                equipment1_uid_combo_box.current(var)

        equipment2_uid_var = t.StringVar(value=foreign_keys[4][0])
        equipment2_uid_combo_box = ttk.Combobox(
            center_frame,
            values=foreign_keys[4],
            textvariable=equipment2_uid_var,
            state="readonly"
        )
        equipment2_uid_combo_box.grid(row=11, column=2, pady=5)
        for var in range(len(foreign_keys[4])):
            if foreign_keys[4][var] == very_massive[number][10]:
                equipment2_uid_combo_box.current(var)

        global focus
        focus = False

        def set_focus1(event):
            global focus
            focus = True

        def set_focus2(event):
            global focus
            focus = False

        date_start_var = t.StringVar()
        date_start_entry = t.Entry(
            center_frame,
            validate="key",
            textvariable=date_start_var,
            validatecommand=check_date
        )
        date_start_entry.grid(row=12, column=2, pady=5)
        date_start_entry.bind("<FocusIn>", set_focus1, '+')
        date_start_entry.bind("<FocusOut>", set_focus2, '+')
        date_start_entry.bind("<KeyRelease>", v.date, '+')
        date_start_entry.insert(0, very_massive[number][11])

        date_finish_var = t.StringVar()
        date_finish_entry = t.Entry(
            center_frame,
            validate="key",
            textvariable=date_finish_var,
            validatecommand=check_date
        )
        date_finish_entry.grid(row=13, column=2, pady=5)
        date_finish_entry.bind("<FocusIn>", set_focus1, '+')
        date_finish_entry.bind("<FocusOut>", set_focus2, '+')
        date_finish_entry.bind("<KeyRelease>", v.date, '+')
        date_finish_entry.insert(0, very_massive[number][12])

        def next_page():
            global number
            number += 1
            if number >= len(very_massive):
                number = 0
            for var in range(len(foreign_keys[4])):
                if foreign_keys[4][var] == very_massive[number][10]:
                    equipment2_uid_combo_box.current(var)
                if foreign_keys[4][var] == very_massive[number][9]:
                    equipment1_uid_combo_box.current(var)
            for var in range(len(foreign_keys[3])):
                if foreign_keys[3][var] == very_massive[number][7]:
                    material2_uid_combo_box.current(var)
                if foreign_keys[3][var] == very_massive[number][5]:
                    material1_uid_combo_box.current(var)
            for var in range(len(foreign_keys[2])):
                if foreign_keys[2][var] == very_massive[number][4]:
                    worker2_uid_combo_box.current(var)
                if foreign_keys[2][var] == very_massive[number][3]:
                    worker1_uid_combo_box.current(var)
            for var in range(len(foreign_keys[1])):
                if foreign_keys[1][var] == very_massive[number][2]:
                    work_uid_combo_box.current(var)
            for var in range(len(foreign_keys[0])):
                if foreign_keys[0][var] == very_massive[number][1]:
                    client_uid_combo_box.current(var)
            date_start_entry.delete(0, t.END)
            date_start_entry.insert(0, very_massive[number][11])
            date_finish_entry.delete(0, t.END)
            date_finish_entry.insert(0, very_massive[number][12])
            material1_count_entry.delete(0, t.END)
            material1_count_entry.insert(0, very_massive[number][6])
            material2_count_entry.delete(0, t.END)
            material2_count_entry.insert(0, very_massive[number][8])
            order_uid_entry.delete(0, t.END)
            order_uid_entry.insert(0, very_massive[number][0])

        def prev_page():
            global number
            number = number - 1
            if number < 0:
                number = len(very_massive) - 1
            for var in range(len(foreign_keys[4])):
                if foreign_keys[4][var] == very_massive[number][10]:
                    equipment2_uid_combo_box.current(var)
                if foreign_keys[4][var] == very_massive[number][9]:
                    equipment1_uid_combo_box.current(var)
            for var in range(len(foreign_keys[3])):
                if foreign_keys[3][var] == very_massive[number][7]:
                    material2_uid_combo_box.current(var)
                if foreign_keys[3][var] == very_massive[number][5]:
                    material1_uid_combo_box.current(var)
            for var in range(len(foreign_keys[2])):
                if foreign_keys[2][var] == very_massive[number][4]:
                    worker2_uid_combo_box.current(var)
                if foreign_keys[2][var] == very_massive[number][3]:
                    worker1_uid_combo_box.current(var)
            for var in range(len(foreign_keys[1])):
                if foreign_keys[1][var] == very_massive[number][2]:
                    work_uid_combo_box.current(var)
            for var in range(len(foreign_keys[0])):
                if foreign_keys[0][var] == very_massive[number][1]:
                    client_uid_combo_box.current(var)
            date_start_entry.delete(0, t.END)
            date_start_entry.insert(0, very_massive[number][11])
            date_finish_entry.delete(0, t.END)
            date_finish_entry.insert(0, very_massive[number][12])
            material1_count_entry.delete(0, t.END)
            material1_count_entry.insert(0, very_massive[number][6])
            material2_count_entry.delete(0, t.END)
            material2_count_entry.insert(0, very_massive[number][8])
            order_uid_entry.delete(0, t.END)
            order_uid_entry.insert(0, very_massive[number][0])

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
            con.change_ord((order_uid_entry.get(), client_uid_var.get(), work_uid_var.get(), worker1_uid_var.get(),
                            worker2_uid_var.get(), material1_uid_var.get(), material1_count_entry.get(),
                            material2_uid_var.get(), material2_count_entry.get(), equipment1_uid_var.get(),
                            equipment2_uid_var.get(), date_start_entry.get(), date_finish_entry.get()))
            global very_massive
            very_massive = con.extract("Order")
            global number
            number = 0
            next_page()
            prev_page()

        def update_info():
            global very_massive
            very_massive = con.extract("Order")
            next_page()
            prev_page()

        def add_info():
            con.create_ord((order_uid_entry.get(), client_uid_var.get(), work_uid_var.get(), worker1_uid_var.get(),
                            worker2_uid_var.get(), material1_uid_var.get(), material1_count_entry.get(),
                            material2_uid_var.get(), material2_count_entry.get(), equipment1_uid_var.get(),
                            equipment2_uid_var.get(), date_start_entry.get(), date_finish_entry.get()))
            global very_massive
            very_massive = con.extract("Order")
            global number
            number = 0
            next_page()
            prev_page()

        def delete_info():
            con.delete("Order", order_uid_entry.get())
            global very_massive
            very_massive = con.extract("Order")
            global number
            number = 0
            next_page()
            prev_page()

        add = t.Button(
            secondary_frame,
            command=add_info
        )
        add.configure(text="Добавить новую запись")
        add.grid(row=1, column=3)

        delete = t.Button(
            secondary_frame,
            command=delete_info
        )
        delete.configure(text="Удалить запись")
        delete.grid(row=1, column=4)

        change = t.Button(
            secondary_frame,
            command=change_info
        )
        change.configure(text="Сохранить запись")
        change.grid(row=1, column=2)

        update = t.Button(
            secondary_frame,
            command=update_info
        )
        update.configure(text="Обновить поля")
        update.grid(row=1, column=1)

    show_form()
    t.mainloop()
