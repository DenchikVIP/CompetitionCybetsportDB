import sqlite3 as sq

connection = None
try:
    connection = sq.connect("Flats.db")
    print("Успешное соединение")
except sq.Error as e:
    print(f"Произошла ошибка '{e}'")


def extract(name):
    cursor = connection.cursor()
    cursor.execute(f"""SELECT * FROM "{name}" """)
    mass = cursor.fetchall()
    for i in range(len(mass)):
        lst = list(mass[i])
        for j in range(len(mass[1])):
            if mass[i][j] is None:
                lst[j] = ""
        mass[i] = tuple(lst)
    return mass


def create_cl(group):
    allow = True
    cursor = connection.cursor()
    cursor.execute(f"Select UID From Client")
    for var in cursor.fetchall():
        if str(group[0]) == str(var[0]):
            allow = False
    if allow:
        cursor.execute(f"""INSERT INTO Client(UID,FIO,"Phone number") VALUES({group[0]}, "{group[1]}", "{group[2]}")""")
        connection.commit()


def change_cl(group):
    exists = False
    cursor = connection.cursor()
    cursor.execute(f"Select UID From Client")
    for var in cursor.fetchall():
        if str(group[0]) == str(var[0]):
            exists = True
    if exists:
        cursor.execute(
            f"""Replace INTO Client(UID,FIO,"Phone number")
            VALUES({group[0]}, "{group[1]}", "{group[2]}")""")
    else:
        cursor.execute(f"""INSERT INTO Client(UID,FIO,"Phone number") VALUES({group[0]}, "{group[1]}", "{group[2]}")""")
    connection.commit()


def create_eq(group):
    allow = True
    cursor = connection.cursor()
    cursor.execute(f"Select UID From Equipment")
    boolst = 0
    if group[2] == "Ручной":
        boolst = 0
    elif group[2] == "Стационарный":
        boolst = 1
    for var in cursor.fetchall():
        if str(group[0]) == str(var[0]):
            allow = False
    if allow:
        cursor.execute(f"""INSERT INTO Equipment(UID,Name,Stationary) VALUES({group[0]}, "{group[1]}", "{boolst}")""")
        connection.commit()


def change_eq(group):
    exists = False
    cursor = connection.cursor()
    cursor.execute(f"Select UID From Equipment")
    boolst = 0
    if group[2] == "Ручной":
        boolst = 0
    elif group[2] == "Стационарный":
        boolst = 1
    for var in cursor.fetchall():
        if str(group[0]) == str(var[0]):
            exists = True
    if exists:
        cursor.execute(
            f"""Replace INTO Equipment(UID,Name,Stationary)
            VALUES({group[0]}, "{group[1]}", "{boolst}")""")
    else:
        cursor.execute(f"""INSERT INTO Equipment(UID,Name,Stationary) VALUES({group[0]}, "{group[1]}", "{group[2]}")""")
    connection.commit()


def create_ord(group):
    allow = True
    cursor = connection.cursor()
    cursor.execute(f"""Select OrderUID From "Order" """)
    for var in cursor.fetchall():
        if str(group[0]) == str(var[0]):
            allow = False
    if allow:
        cursor.execute(
            f"""INSERT INTO Order(OrderUID,ClientUID,WorkUID,Worker1UID,Worker2UID,Material1UID,
            Material1count,Material2UID,Material2count,Equipment1UID,Equipment2UID,Datestart,Datefinish)
            VALUES({group[0]}, "{group[1]}", "{group[2]}", "{group[3]}", "{group[4]}",
            "{group[5]}", "{group[6]}", "{group[7]}", "{group[8]}", "{group[9]}",
            "{group[10]}", "{group[11]}", "{group[12]}")""")
        connection.commit()


def change_ord(group):
    exists = False
    cursor = connection.cursor()
    cursor.execute(f"""Select OrderUID From "Order" """)
    for var in cursor.fetchall():
        if str(group[0]) == str(var[0]):
            exists = True
    if exists:
        cursor.execute(
            f"""Replace INTO "Order"(OrderUID,ClientUID,WorkUID,Worker1UID,Worker2UID,Material1UID,
            Material1count,Material2UID,Material2count,Equipment1UID,Equipment2UID,Datestart,Datefinish)
            VALUES({group[0]}, "{group[1]}", "{group[2]}", "{group[3]}", "{group[4]}",
            "{group[5]}", "{group[6]}", "{group[7]}", "{group[8]}", "{group[9]}",
            "{group[10]}", "{group[11]}", "{group[12]}")""")
    else:
        cursor.execute(f"""INSERT INTO "Order"(OrderUID,ClientUID,WorkUID,Worker1UID,Worker2UID,Material1UID,
            Material1count,Material2UID,Material2count,Equipment1UID,Equipment2UID,Datestart,Datefinish)
            VALUES({group[0]}, "{group[1]}", "{group[2]}", "{group[3]}", "{group[4]}",
            "{group[5]}", "{group[6]}", "{group[7]}", "{group[8]}", "{group[9]}",
            "{group[10]}", "{group[11]}", "{group[12]}")""")
    connection.commit()


def create_wrk(group):
    allow = True
    cursor = connection.cursor()
    cursor.execute(f"Select UID From Work")
    for var in cursor.fetchall():
        if str(group[0]) == str(var[0]):
            allow = False
    if allow:
        cursor.execute(f"""INSERT INTO Work(UID,Name,Cost) VALUES({group[0]}, "{group[1]}", "{group[2]}")""")
        connection.commit()


def change_wrk(group):
    exists = False
    cursor = connection.cursor()
    cursor.execute(f"Select UID From Work")
    for var in cursor.fetchall():
        if str(group[0]) == str(var[0]):
            exists = True
    if exists:
        cursor.execute(
            f"""Replace INTO Work(UID,Name,Cost)
            VALUES({group[0]}, "{group[1]}", "{group[2]}")""")
    else:
        cursor.execute(f"""INSERT INTO Work(UID,Name,Cost) VALUES({group[0]}, "{group[1]}", "{group[2]}")""")
    connection.commit()


def create_mat(group):
    allow = True
    cursor = connection.cursor()
    cursor.execute(f"Select UID From Material")
    for var in cursor.fetchall():
        if str(group[0]) == str(var[0]):
            allow = False
    if allow:
        cursor.execute(
            f"""INSERT INTO Material(UID,Name,Costbyunit,"Unit of measurment")
            VALUES({group[0]}, "{group[1]}", "{group[2]}", "{group[3]}")""")
        connection.commit()


def change_mat(group):
    exists = False
    cursor = connection.cursor()
    cursor.execute(f"Select UID From Material")
    for var in cursor.fetchall():
        if str(group[0]) == str(var[0]):
            exists = True
    if exists:
        cursor.execute(
            f"""Replace INTO Material(UID,Name,Costbyunit,"Unit of measurment")
            VALUES({group[0]}, "{group[1]}", "{group[2]}", "{group[3]}")""")
    else:
        cursor.execute(
            f"""INSERT INTO Material(UID,Name,Costbyunit,"Unit of measurment")
            VALUES({group[0]}, "{group[1]}", "{group[2]}", "{group[3]}")""")
    connection.commit()


def create_wrkr(group):
    allow = True
    cursor = connection.cursor()
    cursor.execute(f"Select UID From Worker")
    for var in cursor.fetchall():
        if str(group[0]) == str(var[0]):
            allow = False
    if allow:
        cursor.execute(
            f"""INSERT INTO Worker(UID,FIO,"Phonenumber","Assignment 1","Assignment 2","Assignment 3")
            VALUES({group[0]}, "{group[1]}", "{group[2]}", "{group[3]}", "{group[4]}", "{group[5]}")""")
        connection.commit()


def change_wrkr(group):
    exists = False
    cursor = connection.cursor()
    cursor.execute(f"Select UID From Worker")
    for var in cursor.fetchall():
        if str(group[0]) == str(var[0]):
            exists = True
    if exists:
        cursor.execute(
            f"""Replace INTO Worker(UID,FIO,"Phonenumber","Assignment 1","Assignment 2","Assignment 3")
            VALUES({group[0]}, "{group[1]}", "{group[2]}", "{group[3]}", "{group[4]}", "{group[5]}")""")
    else:
        cursor.execute(
            f"""INSERT INTO Worker(UID,FIO,"Phonenumber","Assignment 1","Assignment 2","Assignment 3")
            VALUES({group[0]}, "{group[1]}", "{group[2]}", "{group[3]}", "{group[4]}", "{group[5]}")""")
    connection.commit()


def delete(name, delete_id):
    uid = "UID"
    if name == "Order":
        uid = "OrderUID"
    cursor = connection.cursor()
    cursor.execute(f"""DELETE FROM "{name}" WHERE "{uid}"="{delete_id}" """)
    connection.commit()


def foreign_keys():
    cursor = connection.cursor()
    cursor.execute(f"Select UID From Material")
    mat = cursor.fetchall()
    promat = list(mat)
    for var in range(len(promat)):
        promat[var] = promat[var][0]
    mat = tuple(promat)
    cursor.execute(f"Select UID From Client")
    cl = cursor.fetchall()
    procl = list(cl)
    for var in range(len(procl)):
        procl[var] = procl[var][0]
    cl = tuple(procl)
    cursor.execute(f"Select UID From Work")
    wrk = cursor.fetchall()
    prowrk = list(wrk)
    for var in range(len(prowrk)):
        prowrk[var] = prowrk[var][0]
    wrk = tuple(prowrk)
    cursor.execute(f"Select UID From Worker")
    wrkr = cursor.fetchall()
    prowrkr = list(wrkr)
    for var in range(len(prowrkr)):
        prowrkr[var] = prowrkr[var][0]
    wrkr = tuple(prowrkr)
    cursor.execute(f"Select UID From Equipment")
    eq = cursor.fetchall()
    proeq = list(eq)
    for var in range(len(proeq)):
        proeq[var] = proeq[var][0]
    eq = tuple(proeq)
    return (cl, wrk, wrkr, mat, eq)
