import os
import shutil


def copy_items(src, dest):
    folder_list = os.listdir(src)

    file_list = []

    for folder in folder_list:
        for file in os.listdir(src + folder):
            print(folder)
            print(file)
            shutil.copy(src + folder + '/' + file + '/', dest + '/')
            print(file_list)
