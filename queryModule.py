import sqlite3
from sqlite3 import Error

#Функция для создания подключения к файлу БД
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Успешное выполнение")
    except Error as e:
        print(f"Ошибка '{e}'")
    return connection

#Функция для реализации запросов пользователей на создание и добавление данных
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Успешное выполнение")
    except Error as e:
        print(f"Ошибка '{e}'")


#Функция для реализации запросов пользователей на вывод информации
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"Ошибка '{e}'")
