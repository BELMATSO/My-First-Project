# file handling example 1

import os

file = open("C:/Users/HP/Desktop/file handling.txt", "w")
file.close()

# file handling example 2
import os
file = open("C:/Users/HP/Desktop/my files.txt", "r")
print(file.read())
file.close()

