# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def cool_path(path):
    *path, name = path.split('\\')
    path = '\\'.join(path)
    name, extension = name.split('.')
    return (path, name, extension)


path = 'C:\\Users\\master\\Desktop\\python\\homework_05\\task1.py'

print(cool_path(path))