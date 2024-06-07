import os
import shutil
from pathlib import Path
import logging

#Make a list of files to be stored using this program
file_types = {
    'Images': [".jpg",".jpeg", "png"],
    'Documents': [".txt", "docx", ".xlsx"],
    'Videos': [".mp4", ".mov", ".avi"],
    'Music': [".mp3", ".wav", ".aac"],
    'Archives': [".zip", ".rar", ".tar", ".gz"],
    'Apps': [".exe"],
    'Programming': [".py", ".js", ".html", ".css"],
}

#Define path that will feed this file sorter its new files to sort
base_dir = Path("c:/Users/kingz/Downloads/")

#Create the folders which in the folders will be saved
def folder_names():
    for folder in file_types.keys():
        folder_path = base_dir/folder
        folder_path.mkdir(exist_ok = True)

folder_names()

#Logs the files being moved 
logging.basicConfig(filename='file_sorter.log', level=logging.INFO, format='%(asctime)s - %(message)s')

#Function to sort files
def sort_files():
    for file in base_dir.iterdir():
        if file.is_file():
            try:
                file_extension = file.suffix.lower()
                moved = False
                for folder, extensions in file_types.items():
                    if file_extension in extensions:
                         shutil.move(str(file), str(base_dir /folder/file.name))
                         logging.info(f'Moved file: {file.name} to {folder}')
                         moved = True
                         break
                if not moved:
                    logging.warning(f'No category found for file: {file.name}')
            except Exception as e:
                logging.error(f'Error moving file {file.name}: {e}')
                
sort_files()


    