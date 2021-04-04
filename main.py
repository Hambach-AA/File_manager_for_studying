from tkinter import filedialog
from tkinter import *
import os
import shutil
import datetime
import json

class discipline:
    # main_path_lecture = r'C:\Users\hambach\Desktop\Test\Лекции'
    # main_path_practice = r'C:\Users\hambach\Desktop\Test\Практики'

    main_path_lecture = r'D:\Учёба 2.0\Лекции' # Директория где хранятся лекции
    main_path_practice = r'D:\Учёба 2.0\Практики' # Директория где хранятся практики

    def __init__(self,name,semester,number_lectures = None,number_practice= None,lecture_path= None,practice_path= None):

        self.name = name  # Название Дисциплины
        self.semester = semester  # Номер семестра
        if number_lectures == None:
            self.number_lectures = 1  # Номер лекции
            self.number_practice = 1  # Номер практики

            self.lecture_path = self.main_path_lecture + "\\" + name  # Создание пути к папке лекции
            self.practice_path = self.main_path_practice + "\\" + name  # Создание пути к папке практики

            try:
                os.mkdir(self.lecture_path)  # Создание папки лекции
                os.mkdir(self.practice_path)  # Создание папки практики
            except FileExistsError:
                0

            self.lecture_path = self.lecture_path + "\\" + semester  # Создание пути к папке семестр для лекции
            self.practice_path = self.practice_path + "\\" + semester  # Создание пути к папке семестр для практики

            try:
                os.mkdir(self.lecture_path)  # Создание папки семестр для лекции
                os.mkdir(self.practice_path)  # Создание папки семестр для практики
            except FileExistsError:
                print("Данная дисциплина уже была создана ранее")
                self.name = "del"
        else:
            self.number_lectures = number_lectures  # Номер лекции
            self.number_practice = number_practice  # Номер практики

            self.lecture_path = lecture_path  # Создание пути к папке лекции
            self.practice_path = practice_path  # Создание пути к папке практики

    def __path_new_name(self,path, new_name):  # Метод возвращает путь с новым именем файла (фалй не переменовывается)

        for i in range(len(path)):
            if path[-i]== '/':
                return path[0:-i+1]+new_name+path[-3:]

    def __path_new_directory(self,path,new_name):  # Метод возвращает путь с новым именем дериктории
        for i in range(len(path)):
            if path[-i]== '/':
                return path[0:-i+1]+new_name

    def __date(self):  # Метод возвращает текущюю дату


        # day = datetime.datetime.now().day
        # month = datetime.datetime.now().month
        # year = datetime.datetime.now().year

        date = str(datetime.datetime.now().date())   # Получение даты
        date_day_month_year = date[8:] + "." + date[5:7] + "." + date[:4]   # Преоброзование в вид dd.mm.yyyy
        time = (str(datetime.datetime.now().time())[0:-7]).replace(":","፡")  # Получение времени, Преоброзование в вид hh.mm.ss

        # return "{}.{}.{} - {}".format(day,month,year, time)

        return "{} - {}".format(date_day_month_year, time)
    def new_lecture_video(self):  # Метод перемещает переименовывает файл лекции в соответствующую директорию

        root = Tk()  # Создание диалогового окна
        root.withdraw()
        root.filename =  filedialog.askopenfilename(initialdir = "D:\Test",title = "Select file",filetypes = (("Лекции","*.mp4"),("Все файлы","*.*")))

        new_name = "Лекция №{}, {}, {}.".format(self.number_lectures,self.name,self.__date())   # Получение имени для лекции
        self.number_lectures += 1  # Увеличиваем счётчик количества лекций
        new_filename = self.__path_new_name(root.filename,new_name)   # Создание абсолютного пути с новым именем

        os.rename(root.filename,new_filename)   # Переименовывание файла

        shutil.copy(new_filename,self.lecture_path)   # Копирование файла в соответствующую директорию

        os.remove(new_filename)   # Удаление файла

    def not_new_lecture_video(self):  # Метод перемещает переименовывает файл лекции в соответствующую директорию с своей датой

        root = Tk()  # Создание диалогового окна
        root.withdraw()
        root.filename =  filedialog.askopenfilename(initialdir = "D:\Test",title = "Select file",filetypes = (("Лекции","*.mp4"),("Все файлы","*.*")))
        print("Введите номер лекции")
        number = input()
        print("Введите дату")
        new_name = "Лекция №{}, {}, {}.".format(number,self.name,input())   # Получение имени для лекции
        self.number_lectures += 1  # Увеличиваем счётчик количества лекций
        new_filename = self.__path_new_name(root.filename,new_name)   # Создание абсолютного пути с новым именем

        os.rename(root.filename,new_filename)   # Переименовывание файла

        shutil.copy(new_filename,self.lecture_path)   # Копирование файла в соответствующую директорию

        os.remove(new_filename)   # Удаление файла

    def new_practice_video(self):   # Метод перемещает переименовывает файл практики в соответствующую директорию

        root = Tk()  # Создание диалогового окна
        root.withdraw()
        root.filename = filedialog.askopenfilename(initialdir = "D:\Test", title="Select file", filetypes=(("Лекции", "*.mp4"), ("Все файлы", "*.*")))

        new_name = "Практика №{}, {}, {}.".format(self.number_practice, self.name, self.__date())  # Получение имени для практики
        self.number_practice+=1  # Увеличиваем счётчик количества практик
        new_filename = self.__path_new_name(root.filename, new_name)  # Создание абсолютного пути с новым именем

        os.rename(root.filename, new_filename)  # Переименовывание файла

        shutil.copy(new_filename, self.practice_path)  # Копирование файла в соответствующую директорию

        os.remove(new_filename)  # Удаление файла

    def not_new_practice_video(self):   # Метод перемещает переименовывает файл практики в соответствующую директорию с своей датой

        root = Tk()  # Создание диалогового окна
        root.withdraw()
        root.filename = filedialog.askopenfilename(initialdir = "D:\Test", title="Select file", filetypes=(("Лекции", "*.mp4"), ("Все файлы", "*.*")))
        print("Введите номер практики")
        number = input()
        print("Введите дату")
        new_name = "Практика №{}, {}, {}.".format(number, self.name, input())  # Получение имени для практики
        self.number_practice+=1  # Увеличиваем счётчик количества практик
        new_filename = self.__path_new_name(root.filename, new_name)  # Создание абсолютного пути с новым именем

        os.rename(root.filename, new_filename)  # Переименовывание файла

        shutil.copy(new_filename, self.practice_path)  # Копирование файла в соответствующую директорию

        os.remove(new_filename)  # Удаление файла

    def new_practice_lab(self):  # Метод перемещает директорию с lab в нужную директорию

        root = Tk()  # Создание диалогового окна
        root.withdraw()
        root.filename = filedialog.askdirectory(initialdir = "D:\Test")

        print("Введите номер lab")

        lab_number = input()

        new_name = "Lab №{}, {}, {}.".format(lab_number,self.name,self.__date())  # Создание имени директории

        shutil.copytree(root.filename,self.practice_path+"\\"+new_name)  # Копирование директории с файлами

        shutil.rmtree(root.filename)  # Удалени директории

    def not_new_practice_lab(self):  # Метод перемещает директорию с lab в нужную директорию с своей датой

        root = Tk()  # Создание диалогового окна
        root.withdraw()
        root.filename = filedialog.askdirectory(initialdir = "D:\Test")

        print("Введите номер lab")

        lab_number = input()
        print("Введите дату")
        new_name = "Lab №{}, {}, {}.".format(lab_number,self.name,input())  # Создание имени директории

        shutil.copytree(root.filename,self.practice_path+"\\"+new_name)  # Копирование директории с файлами

        shutil.rmtree(root.filename)  # Удалени директории

    def new_lecture_materials(self):

        root = Tk()  # Создание диалогового окна
        root.withdraw()
        root.filenames = filedialog.askopenfilenames(initialdir="D:\Test")

        print("1 - Дополнить материал, 2- Создать материал")    # Информация о командах
        command = input()

        if command == "1":     # Дополнение папки где хранится материал

            listdir = os.listdir(self.lecture_path)     # Создания списка файлов и папок директории
            materials_id = []     # ID папок материалов в директории

            print("Введите номер материала, который хотите дополнить")

            for i in range(len(listdir)):   # Получение списка материалов
                if listdir[i][:8]=="Материал":
                    materials_id.append([i,listdir[i]])      # Добавляется список где глобальный ID в listdir и имя папки материала
                    print("{} - {}".format(i+1,listdir[i]))     # Вывод имени папки

            command = int(input())      # Получение номера папки (с экрана)

            for i in root.filenames:      # В цикле файлы перемещаются в выбранную ранее директорию

                shutil.copy(i, self.lecture_path + "\\" + listdir[materials_id[command-1][0]])  # Копирование копирование файла в директорию

                os.remove(i) # Удаление файла

        elif command == "2":     # Команда создает новую папку материала и копирует туда выбранные файлы

            print("Введите название материала(ов)")

            materials = input()      # Получение имени материала

            #new_name = "Материал(ы) - {}, {}, {}.".format(materials, self.name, self.__date())  # Создание имени директории
            new_name = "Материал(ы) - {}, {}.".format(materials, self.name)  # Создание имени директории
            os.mkdir(self.lecture_path + "\\" + new_name)     # Создание папки материала

            for i in root.filenames:      # В цикле файлы перемещаются в выбранную ранее директорию

                shutil.copy(i, self.lecture_path + "\\" + new_name)  # Копирование копирование файла в директорию

                os.remove(i) # Удаление файла

    def new_practice_materials(self):

        root = Tk()  # Создание диалогового окна
        root.withdraw()
        root.filenames = filedialog.askopenfilenames(initialdir="D:\Test")

        print("1 - Дополнить материал, 2- Создать материал")  # Информация о командах
        command = input()

        if command == "1":  # Дополнение папки где хранится материал

            listdir = os.listdir(self.practice_path)  # Создания списка файлов и папок директории
            materials_id = []  # ID папок материалов в директории

            print("Введите номер материала, который хотите дополнить")

            for i in range(len(listdir)):  # Получение списка материалов
                if listdir[i][:8] == "Материал":
                    materials_id.append(
                        [i, listdir[i]])  # Добавляется список где глобальный ID в listdir и имя папки материала
                    print("{} - {}".format(i + 1, listdir[i]))  # Вывод имени папки

            command = int(input())  # Получение номера папки (с экрана)

            for i in root.filenames:  # В цикле файлы перемещаются в выбранную ранее директорию

                shutil.copy(i, self.practice_path + "\\" + listdir[
                    materials_id[command - 1][0]])  # Копирование копирование файла в директорию

                os.remove(i)  # Удаление файла

        elif command == "2":  # Команда создает новую папку материала и копирует туда выбранные файлы

            print("Введите название материала(ов)")

            materials = input()  # Получение имени материала

            new_name = "Материал(ы) - {}, {}, {}.".format(materials, self.name,
                                                          self.__date())  # Создание имени директории

            os.mkdir(self.practice_path + "\\" + new_name)  # Создание папки материала

            for i in root.filenames:  # В цикле файлы перемещаются в выбранную ранее директорию

                shutil.copy(i, self.practice_path + "\\" + new_name)  # Копирование копирование файла в директорию

                os.remove(i)  # Удаление файла

    def list_data(self):    # Метод возвращает всю инвормацию об экземпляре класса

        return [self.name, self.semester, self.number_lectures,self.number_practice,self.lecture_path,self.practice_path]

def recording(discipline_list): # Функция выполняет запись данных в файл, в формате json
    data_info = []

    for i in range(len(discipline_list)):
        if discipline_list[i].list_data()[0] != "del":
            data_info.append(discipline_list[i].list_data())

    data = json.dumps(data_info)
    file = open("discipline.txt", "w")
    file.write(data)
    file.close()

def editing_disciplines(discipline_list):   # Функция выполняет роль редактирования дисциплины
    discipline_semester = []
    print("Введите семестр")
    semester = input()
    for i in range(len(discipline_list)):
        if discipline_list[i].semester == semester + " Семестр":
            discipline_semester.append(i)

    for i in range(len(discipline_semester)):
        print("{} - {}".format(i + 1, discipline_list[discipline_semester[i]].name))

    print("Введите номер дисциплины")
    discipline_number = int(input())
    print("Информация о предмете")
    print(
        "Количество лекций: {}".format(discipline_list[discipline_semester[discipline_number - 1]].number_lectures - 1))
    print("Количество практик: {}\n".format(
        discipline_list[discipline_semester[discipline_number - 1]].number_practice - 1))
    print("1 - Изменить количество лекций, 2 - Изменить количество практик, 0 - вернутся обратно")
    command = input()
    if command == "1":
        discipline_list[discipline_semester[discipline_number - 1]].number_lectures = int(
            input("Введите новое значение")) + 1
    elif command == "2":
        discipline_list[discipline_semester[discipline_number - 1]].number_practice = int(
            input("Введите новое значение")) + 1

if os.path.exists("discipline.txt"): # Условие проверяет существует ли файл, если да, то считывает из него данные в список

    file = open("discipline.txt", "r")
    data_info = json.load(file)
    file.close()

    discipline_list = []
    for i in range(len(data_info)):
        discipline_list.append(discipline(data_info[i][0],data_info[i][1],data_info[i][2],data_info[i][3],data_info[i][4],data_info[i][5]))

else: # Если нет, то создаст пустую версию списка, которую получает из файла
    discipline_list = []

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n1 - Выбор предмета, 2 - Создание предмета, 3 - Редактирование данных, 0 - выход\n")
    command = input()
    os.system('cls' if os.name == 'nt' else 'clear')
    if command == "1":
        discipline_semester = []
        print("\nВведите семестр")
        semester = input()
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(len(discipline_list)):
            if discipline_list[i].semester == semester+" Семестр":
                discipline_semester.append(i)

        for i in range(len(discipline_semester)):
            print("{} - {}".format(i+1, discipline_list[discipline_semester[i]].name))

        print("\nВведите номер дисциплины")

        discipline_number = int(input())
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n1 - Добавить лекцию, 2 - Добавить практику, 3 - Добавить Lab, 4 - Добавить материал лекции,\n\n6 - Открыть папку лекций, 7 - Открыть папку практик")
        command = input()

        discipline_instance = discipline_list[discipline_semester[discipline_number-1]]     # Экземпляр класса
        if command == "1":
            discipline_instance.new_lecture_video()
            recording(discipline_list)
        elif command == "2":
            discipline_instance.new_practice_video()
            recording(discipline_list)
        elif command == "3":
            discipline_instance.new_practice_lab()
            recording(discipline_list)
        elif command == "4":
            discipline_instance.new_lecture_materials()
            recording(discipline_list)
        elif command == "5":
            discipline_instance.new_practice_materials()
            recording(discipline_list)
        elif command == "6":
            path = os.path.realpath(discipline_list[discipline_semester[discipline_number - 1]].lecture_path)
            os.startfile(path)
        elif command == "7":
            path = os.path.realpath(discipline_list[discipline_semester[discipline_number - 1]].practice_path)
            os.startfile(path)
        elif command == "11":
            discipline_instance.not_new_lecture_video()
            recording(discipline_list)
        elif command == "22":
            discipline_instance.not_new_practice_video()
            recording(discipline_list)
        elif command == "33":
            discipline_instance.not_new_practice_lab()
            recording(discipline_list)


    elif command =="2":

        while True:

            print("Введите название предмета, 0 - вернутся обратно")
            info_1 = input()

            if info_1 == "0":
                print("\n1 - Выбор предмета, 2 - Создание предмета, 0 - выход")
                break

            else:
                print("№ семестра")
                info_2 = input()
                discipline_list.append(discipline(info_1,info_2+" Семестр"))

    elif command == "3":

        editing_disciplines(discipline_list)

    elif command == "0":

        recording(discipline_list)

        break
