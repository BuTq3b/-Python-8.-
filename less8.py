# import sqlite3 as sl
# from easygui import *


# def select_all():
#     cur.execute("SELECT * FROM students;")
#     return cur.fetchall()

# def add_values():
#     cur.execute("INSERT INTO students VALUES (1,'Ваня','Петров');")
#     cur.execute("INSERT INTO students VALUES (2,'Сергей','Сергеев');")

# def select_ivan():
#     cur.execute("SELECT * FROM students WHERE name = 'Ваня';")
#     return cur.fetchall()



# conn = sl.connect("study.db")
# cur = conn.cursor()
# cur.execute("""
#             CREATE TABLE IF NOT EXISTS students
#             (id INTEGER PRIMARY KEY,
#             name TEXT,
#             surname TEXT          
#             );""")

# choice = choicebox("Выберите запрос", "Главная форма", 
#                     ['Все записи', "Только Ваня"])

# if choice == "Все записи":
#     msg = select_all()
#     msgbox(msg, "Результат запроса")
# elif choice == "Только Ваня":
#     msg = select_ivan()
#     msgbox(msg, "Результат запроса")


# conn.commit()
# conn.close()


phonebook = {"дядя Ваня": {'phones': [1212121,5555555],
                           'email': '777@mail.com', 'birthday': '10.10.1990'},
             "дядя Вася": {'phones': [888888]}                         
            }

# print(phonebook['дядя Ваня'])
# print(phonebook['дядя Ваня'] ['phones'])
print(phonebook['дядя Ваня'] ['phones'] [0])

# import json
# contact = {"дядя Ваня": {'phones': [1212121,5555555],
# 'email': '777@mail.com', 'birthday': '10.10.1990'},
# "дядя Вася": {'phones': [888888]}
# }

# contact["Igor"] = {'phones':[440440, 2202220]}

# def save():
#     with open("films.json","w",encoding="utf-8") as fh:
#         fh.write(json.dumps(contact,ensure_ascii=False))
#         print("Nasha biblioteca sohranena")

# def load():
#     with open("films.json","r",encoding="utf-8") as fh:
#         contact=json.load(fh)
#         print("Filmoteca zagrujena")
#     return contact



# while True:
#     command=input("Vvedite comand ")
#     if command=="/start":
#         print("spravochnic nachal rabotu")
#     elif command=="/stop":
#         save()
#         print("spravochnic ostanovil raboty")
#         break
#     elif command=="/all":
#         print("Tekushii spisok filmov")
#         print(contact)
#     elif command =="/add":
#         f=input("Vvedite nazvanie ")
#         contact.append(f)
#         print("Film dobavlen v spisok")
#     elif command=="/find":
#         name = input("Vvedite imia: ")
#         print(contact[name]['phones'])