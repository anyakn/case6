import os

def acceptCommand():
    k = 0
    while k == 0:
        request = input('Пожалуйста, введите номер выбранной команды: ')
        if request not in ['1', '2', '3', '4', '5', '6', '7']:
            print('Ошибка ввода!')
        else:
           k += 1

target = 'Лекция'
path = 'C:\\Users\\karol\\Desktop\\1 семестр'

path_to_files = []
def findFilles(target, path):
    found_files = 0
    for i in os.listdir(path):
        if target.lower() in i.lower():
            found_files += 1
            path_to_files.append(path + '\\' + i)
            print(i)
            if found_files == 0:
                print('Файлы не найдены')
        if os.path.isdir(path + '\\' + i):
            findFilles(target, path + '\\' + i)


print(findFilles(target, path))
print(path_to_files)

