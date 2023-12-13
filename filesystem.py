import os
import ru_local as ru


def acceptCommand():
    '''
    Requests the command number and, if the command number is specified incorrectly,
    displays an error message. Commands are requested until the
    correct command number is entered. Returns the correct command number.
    :return:command
    '''
    k = 0
    while k == 0:
        command = input(ru.accept_с1)
        if command not in ['1', '2', '3', '4', '5', '6', '7']:
            print(ru.accept_с2)
        else:
            k += 1
            command = int(command)
            return command


def runCommand(command):
    '''
    Determines by the command number 'command' which function should be performed.
    :param command: the user enters the number of the command that is wanted to be performed.
    :return:
    '''
    if command == 1:
        path = input(ru.run_c1)
        directory_content(path)
    if command == 2:
        moveUp()
    if command == 3:
        currentDir = input(ru.run_c2)
        moveDown(currentDir)
    if command == 4:
        path = input(ru.run_c3)
        print(countFiles(path))
    if command == 5:
        path = os.getcwd()
        print(countBytes(path))
    if command == 6:
        target = input(ru.run_c4)
        path = input(ru.run_c5)
        print(findFiles(target, path))
    if command == 7:
        return ru.run_c6


def directory_content(path):
    '''
    The function of observing the content of the directory.
    :param path: the path of the directory in which the user wants to observe its content
    (subdirectories, files).
    :return: None
    '''
    for item in os.listdir(path):
        print(item)

def moveUp():
    '''
    The function makes the current parent directory.
    :return: None
    '''
    os.chdir('..')


def moveDown(currentDir):
    '''
    Prompts for the name of a subdirectory.
    If the name is specified correctly, it makes the directory located in currentDir current,
    otherwise it displays an error message
    :param currentDir: new directory
    :return: None
    '''
    go_to = os.getcwd() + '\\' + currentDir
    if os.path.isdir(go_to):
        os.chdir(go_to)
    else:
        print(ru.move_d1)


def countFiles(path):
    '''
    A recursive function that counts the number of files in the specified path directory. All
    files located in subdirectories are included in the calculation.
    :param path: the path of the directory in which the user wants to count the number of files.
    :return: count_files
    '''
    file_count = 0
    if os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            file_count += len(files)
        return file_count
    print(ru.find_f2)


def countBytes(path):
    '''
    A recursive function that calculates the total size (in bytes) of all files in the specified directory path.
    The count includes all files located in subdirectories. Returns the total number of bytes.
    :param path: name of the directory
    :return: count_bytes
    '''
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
    if os.path.isdir(path):
        path_to_files = []
        found_files = 0
        for i in os.listdir(path):
            if target.lower() in i.lower():
                found_files += 1
                path_to_files.append(path + '\\' + i)
                if found_files == 0:
                    print(ru.find_f1)
            if os.path.isdir(path + '\\' + i):
                findFiles(target, path + '\\' + i)
        return path_to_files
    else:
        print(ru.find_f2)


def main():
    while True:
        print(os.getcwd())
        print(ru.main1, ru.main2, ru.main3, ru.main4, ru.main5, ru.main6, ru.main7, sep='\n')
        command = acceptCommand()
        runCommand(command)
        if command == 7:
            print(ru.main8)
            return False


main()
