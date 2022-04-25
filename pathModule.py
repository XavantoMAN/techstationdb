import os
import sys
from sys import platform
#Функция для указания пути к файлу БД
def create_path():
    if platform == "linux" or platform == "linux2":
        File,_ = os.path.split(sys.argv[0])
        File += "/" + "path.txt"
        f = open(File, 'w')
        path = input("Укажите путь где будет располагаться база данных:")
        File,_ = os.path.split(sys.argv[0])
        File += "/" + path
        f.write(File)
        f.close
    elif platform == "darwin":
        File,_ = os.path.split(sys.argv[0])
        File += "path.txt"
        f = open(File, 'w')
        path = input("Укажите путь где будет располагаться база данных:")
        File,_ = os.path.split(sys.argv[0])
        File += path
        f.write(File)
        f.close
    elif platform == "win32":
        File,_ = os.path.split(sys.argv[0])
        File += "path.txt"
        f = open(File, 'w')
        path = input("Укажите путь где будет располагаться база данных:")
        File,_ = os.path.split(sys.argv[0])
        File +=  path
        f.write(File)
        f.close
