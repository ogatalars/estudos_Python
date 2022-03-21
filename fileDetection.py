import os

path = "D:\\Cursos\\uspC\\test.txt"

if os.path.exists(path):
    print("Path exists")
    if os.path.isfile(path):
        print("Path is a file")
else:
    print("Path does not exist")


path2 = "D:\\Cursos\\uspC"

if os.path.exists(path2):
    print("Path exists")
    if os.path.isfile(path2):
        print("path is a file")
else:
    print("Path does not exist")
