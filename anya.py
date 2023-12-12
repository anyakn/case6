import os


def moveDown(currentDir):
    os.chdir(currentDir)
    nextdir = input('Введите имя подкаталога: ')
    go_to = currentDir + '\\' + nextdir
    if os.path.isdir(go_to):
        os.chdir(go_to)
    else:
        print('Ошибка! Такого пути не существует!')


def countBytes(path):
    count_bytes = 0

    for i in os.listdir(path):
        new_path = path + '\\' + i
        if os.path.isfile(new_path):
            count_bytes += os.path.getsize(new_path)
        elif os.path.isdir(new_path):
            count_bytes += countBytes(new_path)

    return count_bytes


import os


def main():
    while True:
        print(os.getcwd())
        print('''1. Просмотр каталога
        2. На уровень вверх
        3. На уровень вниз
        4. Количество файлов и каталогов
        5. Размер текущего каталога (в байтах)
        6. Поиск файла
        7. Выход из программы''')

        command = acceptCommand()
        runCommand(command)
        if command == 7:
            print('Работа программы завершена.')
            break

    if __name__ == '__main__':
        main()


def countFiles(path):
    count_files = 0

    for i in os.listdir(path):
        new_path = os.getcwd() + '\\' + i
        if os.path.isfile(new_path):
            count_files += 1
        if os.path.isdir(path):
            count_files += countFiles(new_path)

    return count_files

countFiles('C:\Users\annil\OneDrive\Рабочий стол\history')