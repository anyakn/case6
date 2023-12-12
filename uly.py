import os
def runCommand(command):
    '''
    Determines by the command number 'command' which function should be performed.
    :param command: the user enters the number of the command that is wanted to be performed.
    :return: None
    '''
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
    '''
    The function makes the current parent directory/
    :return: None
    '''
    os.chdir('..')

def countFiles(path):
    '''
    A recursive function that counts the number of files in the specified path directory. All
    files located in subdirectories are included in the calculation.
    :param path: the path of the directory in which the user wants to count the number of files.
    :return: file_count
    '''
    file_count = 0

    for files in os.walk(path):
        file_count += len(files)

    return file_count

'''
Функция chdir() модуля os изменяет текущий рабочий каталог. 
Аргумент path может принимать объекты, представляющие путь файловой системы
'''