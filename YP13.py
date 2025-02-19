import sqlite3

#Подключение к бд
connection = sqlite3.connect("my_database.db")
connection.close()
