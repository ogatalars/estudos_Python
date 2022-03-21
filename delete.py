import os
import shutil

path = 'delete.txt'

os.remove(path)


try:
    #     os.remove(path)
    os.rmdir(path)
except FileNotFoundError:
    print("The file does not exist")
except PermissionError:
    print("You don't have permission to delete this file")
else:
    print("The file was deleted")
