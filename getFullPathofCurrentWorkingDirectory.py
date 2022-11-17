#Using pathlib module
import pathlib

#path of the given file
print(pathlib.Path("my_file.txt").parent.absolute())

# current working directory
print(pathlib.Path().absolute())

#Using os module
import os

# path of the given file
print(os.path.dirname(os.path.abspath("my_file.txt")))

# current working directory
print(os.path.abspath(os.getcwd()))