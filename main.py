from sys import platform
import passwordCheck
import queryModule as qm
import os
import pathModule as pm
import sys
#Открывает файл в котором содержиться путь к файлу базы данных
Path,_ = os.path.split(sys.argv[0])
clearing = 'cls'
if platform == "linux" or platform == "linux2":
    Path += "/" + "path.txt"
    clearing = 'clear'
elif platform == "darwin":
    Path += "path.txt"
elif platform == "win32":
    Path += "path.txt"
    clearing = 'cls'
f = open(Path)
path = f.readline()
#Идет проверка условия, если в файле существует путь к файлу то идет подключение, если путь не указан или файл БД не существует то выполняется функция создания пути через модуль. Путь указывает пользователь
if os.path.exists(path):
    pass
else:
    import createModule
#Осуществляется проверка пароля, если верный открывается доступ к взаимодействию, если нет, программа закрывается 
passwordCheck.password_check(input("Введите пароль:"))
os.system(clearing)
connection = qm.create_connection(path)
#Отображает список всех услуг из таблицы
def show_services():
    select_services = "SELECT * from services"
    selected = qm.execute_read_query(connection, select_services)
    for i in selected:
        print(i)
#Отображает список деталей из таблицы
def show_parts():
    select_parts = "SELECT * from parts"
    selected = qm.execute_read_query(connection, select_parts)
    for i in selected:
        print(i)
#Отображает список сотрудников из таблицы
def show_employee():
    select_employee = "SELECT * from employee"
    selected = qm.execute_read_query(connection, select_employee)
    for i in selected:
        print(i)
#Отображает список покупателей из таблицы
def show_customers():
    select_customers = "SELECT * from customers"
    selected = qm.execute_read_query(connection, select_customers)
    for i in selected:
        print(i)
#Отображает список всех оказанных услуг из таблицы
def show_rendered_services():
    select_rendered_services = "SELECT * FROM rendered_services"
    selected = qm.execute_read_query(connection, select_rendered_services)
    for i in selected:
        print(i)

#Реализует удаление выбранной строки из выбранной таблицы
def delete_str():
    print("Укажите из какой таблицы нужно удалить данные")
    print("0.)Отмена")
    table = input("Название таблицы(услуги, детали, сотрудники, клиенты, оказанные услуги):")
    if table == 'Услуги' or table == 'услуги' or table == 'УСЛУГИ':
        table = 'services'
    elif table == 'Детали' or table == 'детали' or table == 'ДЕТАЛИ':
        table = 'parts'
    elif table == 'Сотрудники' or table == 'сотрудники' or table == 'СОТРУДНИКИ':
        table = 'employee'
    elif table == 'Клиенты' or table == 'клиенты' or table == 'КЛИЕНТЫ':
        table = 'customers'
    elif table == 'Оказанные услуги' or table == 'оказанные услуги' or table == 'ОКАЗАННЫЕ УСЛУГИ' or table == 'оказанные_услуги' or table == 'Оказанные_услуги':
        table = 'rendered_services'
    elif table == '0':
        os.system(clearing)
        choose_action()
    number = input("Номер записи:")
    delete_comment = f"DELETE FROM {table} WHERE id = '{number}'"
    qm.execute_query(connection, delete_comment)

#Отображает список таблиц
def show_tables():
    print("services, parts, employee, customers, rendered_services")

    
#Реализует возможность ввода записей в выбранную таблицу
def choose_table():
    print("В какую таблицу следует внести данные ?")
    print("1.)Таблица Услуг")
    print("2.)Таблица деталей")
    print("3.)Таблица сотрудников")
    print("4.)Таблица клиентов")
    print("5.)Таблица Оказанных услуг")
    print("0.)Отмена")
    table = int(input("Таблица номер:"))
    if table == 1:
        name = input("Название услуги:")
        cost = input("Стоимость:") 
        create_services = f"""
        INSERT INTO
            services(name, cost)
        VALUES
            ('{name}', '{cost}');""" 
        qm.execute_query(connection, create_services)
    elif table == 2:
        name = input("Название детали:")
        quantity = input("Число деталей на складе:")
        create_parts = f"""
        INSERT INTO
            parts(name, quantity_in_stock)
        VALUES
            ('{name}', '{quantity}');"""
        qm.execute_query(connection, create_parts)
    elif table == 3:
        surname = input("Фамилия:")
        name = input("Имя:")
        patronymic = input("Отчество:")
        date = input("Дата рождения:")
        phone = input("Номер телефона:")
        create_employee = f"""
        INSERT INTO
            employee(surname, name, patronymic, date_of_birth, phone)
        VALUES
            ('{surname}', '{name}', '{patronymic}', '{date}', '{phone}');"""
        qm.execute_query(connection, create_employee)
    elif table == 4:
        name = input("Имя:")
        phone = input("Номер телефона:")
        car_brand = input("Марка автомобиля:")
        create_customers = f"""
    INSERT INTO
        customers(name, phone, car_brand)
    VALUES
        ('{name}', '{phone}', '{car_brand}');"""
        qm.execute_query(connection, create_customers)
    elif table == 5:
        service_id = input("id услуги:")
        part_id = input("id детали:")
        employee_id = input("id сотрудника:")
        customer_id = input("id клиента:")
        create_rendered_services = f"""
    INSERT INTO
        rendered_services(service_id, part_id, employee_id, customer_id)
    VALUES
        ('{service_id}', '{part_id}', '{employee_id}', '{customer_id}');"""
        qm.execute_query(connection, create_rendered_services)
    elif table == 0:
        os.system(clearing)
        choose_action()

#Выводит список выбранных деталей
def get_part():
    name = input("Введите название детали которую нужно найти:\n0.)Отмена\n>")
    if name == '0':
        os.system("cls")
        choose_action()
    select_part = f"SELECT DISTINCT id, name, quantity_in_stock from parts WHERE name like '{name}'"
    part = qm.execute_read_query(connection, select_part)
    for i in part:
        print(i)

#Реализует выбор действия по управлению СУБД    
def choose_action():
    print("Выберите действие:")
    print("1.)Просмотр выбранной детали")
    print("2.)Внесение данных в БД")
    print("3.)Посмотреть таблицу услуг")
    print("4.)Посмотреть таблицу деталей")
    print("5.)Посмотреть таблицу сотрудников")
    print("6.)Посмотреть таблицу клиентов")
    print("7.)Посмотреть таблицу оказанных услуг")
    print("8.)Посмотреть список таблиц")
    print("9.)Удалить запись")
    try:
        choose = int(input("Действие:"))
        os.system(clearing)
        if choose == 1:
            get_part()
        elif choose == 2:
            choose_table()
        elif choose == 3:
            show_services()
        elif choose == 4:
            show_parts()
        elif choose == 5:
            show_employee()
        elif choose == 6:
            show_customers()
        elif choose == 7:
            show_rendered_services()
        elif choose == 8:
            show_tables()
        elif choose == 9:
            delete_str()
    except ValueError:
        print("Ну это же не цифра !")
        choose_action()



#Алгоритм неоднократного запуска программы начиная с выбора действия, либо выход из программы
while True:
    choose_action()
    print("Выполнить ещё действие ?(y/n)")
    Try = input()
    if Try == "y" or Try == "Y" or Try == "н" or Try == "Н":
        os.system(clearing)
    else:
        break

print("---------END OF PROGRAMM---------")
print("---------See you Later !---------")
f.close
