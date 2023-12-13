import os
'''''
def runCommand(command):

    if command == 1:

    elif command == 2:
        moveUp()
    elif command == 3:
        moveDown(currentDir)
    elif command == 4:
        countFiles(path)
    elif command == 5:
        countBytes(path)
    elif command == 6:
        findFiles(target, path)
    elif command == 7:
        print('Работа программы завершена.')
        break
    else:
        print('Недопустимый номер команды')



def moveUp():
    os.chdir('..')
'''''


def countFiles(path):
    '''
    A recursive function that counts the number of files in the specified path directory. All
    files located in subdirectories are included in the calculation.
    :param path: the path of the directory in which the user wants to count the number of files.
    :return: file_count
    '''
    file_count = 0

    for root, dirs, files in os.walk(path):
        file_count += len(files)

    return file_count

path = input('Введи: ')
print(countFiles(path))
'''
Функция chdir() модуля os изменяет текущий рабочий каталог. 
Аргумент path может принимать объекты, представляющие путь файловой системы
'''