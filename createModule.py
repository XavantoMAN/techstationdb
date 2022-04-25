#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import platform
import queryModule as qm
import pathModule as pm
import passwordCheck
import sys
import os
Path,_ = os.path.split(sys.argv[0])
if platform == "linux" or platform == "linux2":
    Path += "/" + "path.txt"
elif platform == "darwin":
    Path += "path.txt"
elif platform == "win32":
    Path += "path.txt"
f = open(Path)
path = f.readline()

#Создает запрос на создание таблицы услуг
create_services_table = """
CREATE TABLE IF NOT EXISTS services(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    cost INTEGER NOT NULL
);
"""

#Создает запрос на создание таблицы деталей
create_parts_table = """
CREATE TABLE IF NOT EXISTS parts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    quantity_in_stock INT
);
"""

#Создает запрос на создание таблицы сотрудников
create_employee_table = """
CREATE TABLE IF NOT EXISTS employee(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    surname TEXT NOT NULL,
    name TEXT NOT NULL,
    patronymic TEXT,
    date_of_birth DATE NOT NULL,
    phone TEXT
);
"""

#Создает запрос на создание таблицы клиентов
create_customers_table = """
CREATE TABLE IF NOT EXISTS customers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    car_brand TEXT NOT NULL
);
"""

#Создает запрос на создание таблицы оказанных услуг
create_rendered_services_table = """
CREATE TABLE IF NOT EXISTS rendered_services(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    service_id INTEGER NOT NULL,
    part_id INTEGER,
    employee_id INTEGER NOT NULL,
    customer_id INTEGER NOT NULL,
    FOREIGN KEY (service_id) REFERENCES services(id)
    FOREIGN KEY (part_id) REFERENCES parts(id)
    FOREIGN KEY (employee_id) REFERENCES employee(id)
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);
"""

#Создает запрос на заполнение таблицы услуг
create_services = """
INSERT INTO
    services(id, name, cost)
VALUES
    (NULL, 'Замена масла', 250),
    (NULL, 'Ремонт двигателя', 10000);
"""

#Создает запрос на заполнение таблицы деталей
create_parts = """
INSERT INTO
    parts(id, name, quantity_in_stock)
VALUES
    (NULL, 'Генератор', 20),
    (NULL, 'Двигатель', 30);
"""

#Создает запрос на заполнение таблицы сотрудников
create_employee = """
INSERT INTO
    employee(id, surname, name, patronymic, date_of_birth, phone)
VALUES
    (NULL, 'Родин', 'Иван', 'Степанович', '29.05.1993', +77057244415),
    (NULL, 'Чистяков', 'Тимофей', 'Тимофеевич', '30.12.1998', +77774321544);
"""

#Создает запрос на заполнение таблицы клиентов
create_customers = """
INSERT INTO
    customers(id, name, phone, car_brand)
VALUES
    (NULL, 'Иван', +77474128126, 'audi'),
    (NULL, 'Степан', +77475926743, 'bmw');
"""

passwordCheck.set_password()

#Обращается к модулю для указания пути к файлу
pm.create_path()
#Реализует запрос на подключение к БД по введенному ранее пути
connection = qm.create_connection(path)
#Реализует запросы на создание таблиц
qm.execute_query(connection, create_services_table)
qm.execute_query(connection, create_parts_table)
qm.execute_query(connection, create_employee_table)
qm.execute_query(connection, create_customers_table)
qm.execute_query(connection, create_rendered_services_table)

if sys.argv[1] == 'debug':
    print("Заполение")
    #Реализует запросы на заполнение таблиц
    qm.execute_query(connection, create_services)
    qm.execute_query(connection, create_parts)
    qm.execute_query(connection, create_employee)
    qm.execute_query(connection, create_customers)
else:
    pass
f.close()
