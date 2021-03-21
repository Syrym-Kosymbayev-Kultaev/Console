import os

if os.name == 'nt': # Проверка ОС
    print('Командная строка: ')
else:
    print('Предупреждение!\nПрограмма предназначена для операционной системы Windows')

me = os.getlogin()  # Получение имени пользователя
pat = 'c://Users/{}/Desktop'.format(me)  # Создание пути

def print_help(): # Функция вызова помощи
    print('mkdir - создание папки на Рабочем столе')
    print('rmdir - удаление папки на Рабочем столе')
    print('rename - переименование папки')
    print('help - получение справки')
    print('exit - выход из программы')

def make_dir(): # Функция создания папки
    dir_name = input('Название папки: ')
    if not dir_name:
        print('Необходимо указать название ')
        return
    dir_path = os.path.join(pat, dir_name)
    try: # Проверка на ошибки
        os.mkdir(dir_path) # Создание папки
        print('Папка {} создана'.format(dir_name))
    except FileExistsError:
        print('Папка {} уже существует'.format(dir_name))

def delete_dir(): # Функция удаления папки
    dir_name = input('Название папки: ')
    if not dir_name:
        print('Необходимо указать название')
        return
    dir_path = os.path.join(pat, dir_name)
    try: # Проверка на ошибки
        os.rmdir(dir_path) # Удаление папки
        print('Папка {} удалена'.format(dir_name))
    except FileNotFoundError:
        print('Папки {} не существует'.format(dir_name))

def rename_dir(): # Функция удаления папки
    dir_name = input('Название папки: ')
    dir_name_1 = input('Новое название папки: ')
    if not dir_name:
        print('Необходимо указать название')
        return
    os.chdir(pat)
    try: # Проверка на ошибки
        os.rename(dir_name, dir_name_1) # Удаление папки
        print('Папка {} переименована на {}'.format(dir_name, dir_name_1))
    except FileExistsError:
        print('Папка {} уже существует'.format(dir_name_1))
    except FileNotFoundError:
        print('Папки {} не существует'.format(dir_name))

def look_dir():
    os.chdir(pat)
    print(os.getcwd())

def list_dir():
    os.chdir(pat)
    print([i for i in os.listdir() if os.path.isdir(i)])

do = {'help': print_help, 'mkdir': make_dir, 'rmdir': delete_dir, 'rename': rename_dir, 'look': look_dir, 'list': list_dir } # Словарь для удобства

while True:
     key = input() # Ввод команды
     if key:
        if do.get(key):
            do[key]()
        elif key == 'exit':
            break
        else:
            print('Указана неверная команда')
            print('help - получения справки')
