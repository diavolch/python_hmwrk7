# Напишите функцию группового переименования файлов. Она должна:
# принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# принимать параметр количество цифр в порядковом номере.
# принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# принимать параметр расширение конечного файла.
# принимать диапазон сохраняемого оригинального имени.
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
#
# Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
import os

def rename_files(new_name, digit, old_extension, new_extension, range_name, path='./test'):
    counter = 1
    for filename in os.listdir(path):
        if filename.endswith(old_extension):
            name = filename.split('.')[0]
            renamefile = name[range_name[0]:range_name[1]] if range_name else ''
            # newfilename = renamefile.join(new_name).join(str(counter).zfill(digit)).join('.' + new_extension)
            newfilename = (renamefile + new_name) + str.zfill(str(counter), digit) + '.' + new_extension
            os.rename(os.path.join(path,filename), os.path.join(path, newfilename))
            counter+=1

rename_files('di', 3, 'txt', 'mp3', [0,2])