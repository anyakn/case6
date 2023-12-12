import os


def acceptCommand():
    '''
    Requests the command number and, if the command number is specified incorrectly,
    displays an error message. Commands are requested until the
    correct command number is entered. Returns the correct command number.
    :return:command
    '''
    k = 0
    while k == 0:
        command = input('Пожалуйста, введите номер выбранной команды: ')
        if command not in ['1', '2', '3', '4', '5', '6', '7']:
            print('Ошибка ввода!')
        else:
            k += 1
            command = int(command)
            return command


def runCommand(command):
    if command == 1:
        return 0
    if command == 2:
        moveUp()
    if command == 3:
        currentDir = input('Укажите имя подкатолга: ')
        moveDown(currentDir)
    if command == 4:
        path = input('Укажите имя каталога, в котором хотите узнать количество файлов: ')
        countFiles(path)
    if command == 5:
        path = input('Укажите имя каталога, в котором хотите узнать суммарный объем файлов: ')
        countBytes(path)
    if command == 6:
        target = input('Укажите ключевое слово для поиска файлов с данным словом: ')
        path = input('Укажите имя каталога, в котором хотите осуществить поиск: ')
        findFiles(target, path)
    if command == 7:
        return 'Работа программы завершена.'


def moveUp():
    os.chdir('..')


def moveDown(currentDir):
    os.chdir(currentDir)
    nextdir = input('Введите имя подкаталога: ')
    go_to = currentDir + '\\' + nextdir
    if os.path.isdir(go_to):
        os.chdir(go_to)
    else:
        print('Ошибка! Такого пути не существует!')


def countFiles(path):
    file_count = 0

    for root, dirs, files in os.walk(path):
        file_count += len(files)

    return file_count


def countBytes(path):
    count_bytes = 0

    for i in os.listdir(path):
        new_path = path + '\\' + i
        if os.path.isfile(new_path):
            count_bytes += os.path.getsize(new_path)
        elif os.path.isdir(new_path):
            count_bytes += countBytes(new_path)

    return count_bytes


def findFiles(target, path):
    '''
    A recursive function that generates a list of file paths whose name contains target.
    All subdirectories of the path directory are included in the search. If the files are not found,
    the corresponding message is displayed.
    :param target:
    :param path:
    :return: path_to_files
    '''
    path_to_files = []
    found_files = 0
    for i in os.listdir(path):
        if target.lower() in i.lower():
            found_files += 1
            path_to_files.append(path + '\\' + i)
            print(i)
            if found_files == 0:
                print('Файлы не найдены')
        if os.path.isdir(path + '\\' + i):
            findFiles(target, path + '\\' + i)
    print('Найдено', found_files, 'файлов, содержащих', target)
    return path_to_files


def main():
    while True:
        print(os.getcwd())
        print('1. Просмотр каталога', '2. На уровень вверх', '3. На уровень вниз',
              '4. Количество файлов и каталогов', '5. Размер текущего каталога (в байтах)',
              '6. Поиск файла', '7. Выход из программы', sep='\n')

        command = acceptCommand()
        runCommand(command)
        if command == 7:
            print('Работа программы завершена.')
            return False

    if __name__ == '__main__':
        main()


main()
