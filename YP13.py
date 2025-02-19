import sqlite3

#Подключение к бд
connection = sqlite3.connect("my_database.db")
cursor = connection.cursor()

#Создание таблицы Users
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)
""")
#Сохранение и закрываем соединение
connection.commit()
connection.close()
print(1)
