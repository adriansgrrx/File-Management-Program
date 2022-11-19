# The main idea of this program is to arrange/manage the files that enters my computer to a certain folder.
# Why? For "order"

# Accessing files in python
import os as my_computer

my_downloads = "C:/Users/adrian/Downloads"
# scandir method is used to access the directory of a certain path
for files in my_computer.scandir(my_downloads):
    print(files.name)