
import os 


def find_nested_dir_files(path,dir_name):
    path = path + "/" + dir_name
    my_list = os.listdir(path)

    for dir_file in my_list:
        if os.path.isdir(path+"/"+dir_file):
            print('DIRECTORY : ',dir_file)
            find_nested_dir_files(path,dir_file)
        else:
            print(dir_file)
    print()

  


path = "/home/hp"
print('DIRECTORY : ',"DataGrokr")
my_list = find_nested_dir_files(path,"DataGrokr")

# ('DIRECTORY : ', 'DataGrokr')
# python dir_tree.py
# DG-Intern Training Plan - v0.3.xlsx.ods
# ('DIRECTORY : ', 'Courses')
# ('DIRECTORY : ', 'GitHub')
# GitCommands.odt
# ()
# ('DIRECTORY : ', 'python')
# search.py
# email.py
# divisible57.py
# dir_tree.py
# square.py
# threeD.py
# set.py
# .~lock.pythonAssgn.odt#
# pythonAssgn.odt
# ()
# Unittesting.odt
# ('DIRECTORY : ', 'SQL')
# OneManyRelationNotations.png
# ABS-SQL Assignment.pdf
# SQL_assignment.odt
# SQLdoc.odt
# Posgres_installation.odt
# 011 Screen-Shot-E6-04-17-at-12.22.49-PM.png
# SQLppt.odp
# ()
# ()
# ()