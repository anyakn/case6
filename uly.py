import os
def runCommand(command):
    if command == 1:
        acceptCommand()
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
        print()
    else:
        print('Недопустимый номер команды')



def moveUp():
    os.chdir('..')

def countFiles(path):
    file_count = 0
    for root, dirs, files in os.walk(path):
        file_count += len(files)
    return file_count
