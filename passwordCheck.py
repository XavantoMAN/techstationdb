import sys
import os
from sys import platform
#Функция которая служит для задания пароля системы
def set_password():
    File,_ = os.path.split(sys.argv[0])
    if platform == "linux" or platform == "linux2":
        File += "/" + "password.txt"
    elif platform == "darwin":
        File += "password.txt"
    elif platform == "win32":
        File += "password.txt"
    f = open(File, 'w')
    password = input("Задайте пароль для системы:")
    f.write(password)
    f.close

#Функция служащая для проверки пароля 
def password_check(checked_word):
    File,_ = os.path.split(sys.argv[0])
    if platform == "linux" or platform == "linux2":
        File += "/" + "password.txt"
    elif platform == "darwin":
        File += "password.txt"
    elif platform == "win32":
        File +=  "password.txt"
    f = open(File)
    password = f.read()
    if checked_word != password:
       print("Введен неверный пароль")
       sys.exit()
    else:
        pass

