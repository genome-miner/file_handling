from pathlib import Path
import shutil

class FileOrganizer:
    def __init__(self):
        self.path = Path(input('Give a path: '))

    def path_validation(self):
        while True:
            if self.path.is_absolute() and self.path.exists() and self.path.is_dir():
                print('It is a valid absolute directory path.')
                break
            else:
                print('Invalid path. Write a valid absolute directory path.')
                self.path = Path(input('Give a path: '))

    def file_scanning(self):
        # Scan all files once
        files = [f for f in self.path.iterdir() if f.is_file()]
        print(files)

        # Build folder dictionary dynamically
        folder = {}
        for file in files:
            extension = file.suffix.lower()
            if extension == "":
                folder_name = "NoExtension"
            else:
                folder_name = extension[1:].upper()  # Remove the dot and uppercase

            # Create list if folder doesn't exist
            if folder_name not in folder:
                folder[folder_name] = []
            
            # Append every file to the folder
            folder[folder_name].append(file.name)

        # Move files into folders
        for folder_name, files_list in folder.items():
            folder_path = self.path / folder_name
            folder_path.mkdir(exist_ok=True)
            for file_name in files_list:
                shutil.move(self.path / file_name, folder_path)
                
    def organiztion(self):
        self.path_validation()
        self.file_scanning()
            