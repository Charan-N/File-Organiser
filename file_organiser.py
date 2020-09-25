'''
    Author: Siva Charan N
    GitHub: "https://github.com/Charan-N"
'''

#importing required libraries
import os
from pathlib import Path
import shutil
import time

#creating main directory
main_dir = 'C:/Users/chara/Downloads/'

folder_list = ['PDFs', 'Executables', 'Zips', 'Images', 'Misc'] #list of seperate folders
direc = Path(main_dir)

while True:
    for item in direc.iterdir():
        #checking if separate folders are created or not
        if item.is_dir() and item.name in folder_list:
            continue

        #creating the folder if not present
        else:
            for folder in folder_list:
                new_folder = os.path.join(main_dir, folder)
                try:  
                    os.mkdir(new_folder)  
                except OSError as error:  
                    continue


    #moving into respective folders

    for item in direc.iterdir():

        time.sleep(0.1)

        if item.is_dir():
            continue

        if item.suffix in ['.pdf', '.docx']:
            source = os.path.abspath(item)
            destination = os.path.join(main_dir, 'PDFs')
            shutil.move(source, destination)

        elif item.suffix == '.zip':
            source = os.path.abspath(item)
            destination = os.path.join(main_dir, 'Zips')
            shutil.move(source, destination)
        
        elif item.suffix == '.exe':
            source = os.path.abspath(item)
            destination = os.path.join(main_dir, 'Executables')
            shutil.move(source, destination)
        
        elif item.suffix in ['.jpg', '.png', '.jpeg', '.bmp']:
            source = os.path.abspath(item)
            destination = os.path.join(main_dir, 'Images')
            shutil.move(source, destination)

        else:
            source = os.path.abspath(item)
            destination = os.path.join(main_dir, 'Misc')
            shutil.move(source, destination)