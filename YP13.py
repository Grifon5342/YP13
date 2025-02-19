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
cursor.execute("INSERT INTO Users (username, email, age) VALUES (?, ?, ?)", ("newuser", "newuser@example.com", 28))

#Обновление записей
cursor.execute("UPDATE Users SET age = ? WHERE username = ?", (29, "newuser"))

#Удвление записей
cursor.execute("DELETE FROM Users WHERE username = ?", ("newuser",))

#Выполнение запросов
cursor.execute("SELECT * FROM Users")
users = cursor.fetchall()
#Выводим результат
for user in users:
    print(user)

#Выбираем имена и возраст пользователей старше 25 лет
cursor.execute("SELECT username, age FROM Users WHERE age > ?", (25,))
results = cursor.fetchall()

for row in results:
    print(row)

#Выбираем и сортируем пользователей
cursor.execute("""
SELECT username, age, AVG(age)
FROM Users
GROUP BY age
HAVING AVG(age) > ?
ORDER BY age DESC
""", (30,))
results = cursor.fetchall()

for row in results:
    print(row)

#Подсчет общего числа пользователей
cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]

print("Общее количество пользователей:", total_users)

#Вычисление суммы возвратов пользователей
cursor.execute("SELECT SUM(age) FROM Users")
total_age = cursor.fetchone()[0]

print("Общая сумма возрастов пользователей:", total_age)

#Вычисление среднего возраста пользователей
cursor.execute("SELECT AVG(age) FROM Users")
total_avg = cursor.fetchone()[0]

print("Средний возраст пользователей:", total_avg)

#Нахождение минимального возраста
cursor.execute("SELECT MIN(age) FROM Users")
min_age = cursor.fetchone()[0]

print("Минимальный возраст среди пользователей:", min_age)

#Нахождение максимального возраста
cursor.execute("SELECT MAX(age) FROM Users")
max_age = cursor.fetchone()[0]

print("Максимальный возраст среди пользователей:", max_age)

#Нахождение пользователей с наибольшим возрастом
cursor.execute("""
SELECT username, age
FROM Users
WHERE age = (SELECT MAX(age) FROM Users)
""")
oldest_users = cursor.fetchall()

for user in oldest_users:
    print(user)

#Выбираем всех пользователей
cursor.execute("SELECT * FROM Users")
users = cursor.fetchall()
for user in users:
    print(user)

#Выбор первого пользователя
cursor.execute("SELECT * FROM Users")
first_user = cursor.fetchone()
print(first_user)

#Выбор первых 5 пользователей
cursor.execute("SELECT * FROM Users")
first_five_users = cursor.fetchmany(5)
print(first_five_users)

#Выбор всех пользователей 
cursor.execute("SELECT * FROM Users")
all_users = cursor.fetchall()
print(all_users)
#--------------------------------------------------------------------
#Выбираем всех пользователей
cursor.execute("SELECT * FROM Users")
users = cursor.fetchall()

#Преобразуем результаты в список словарей
users_list = []
user_dict = {}
for user in users:
    user_dict = {
        "id": user[0],
        "username": user[1],
        "email": user[2],
        "age": user[3]
    }
users_list.append(user_dict)

#Выводим результаты
for user in users_list:
    print(user)
#---------------------------------------------------------------------
#Сохранение и закрываем соединение
connection.commit()
connection.close()

