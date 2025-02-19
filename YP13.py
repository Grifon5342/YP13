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

#Создание индекса для столбца "email"
#cursor.execute("CREATE INDEX idx_email ON Users (email)")


#Дабовление нового пользователя
#cursor.execute("INSERT INTO Users (username, email, age) VALUES (?, ?, ?)", ("newuser", "newuser@example.com", 28))

#Выполнение запросов
#cursor.execute("SELECT * FROM Users")
#users = cursor.fetchall()
#Выводим результат
#for user in users:
#    print(user)

#Выбираем имена и возраст пользователей старше 25 лет
cursor.execute("SELECT username, age FROM Users WHERE age > ?", (25,))
results = cursor.fetchall()

for row in results:
    print(row)


#Сохранение и закрываем соединение
connection.commit()
connection.close()

