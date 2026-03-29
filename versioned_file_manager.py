from pathlib import Path
import shutil
import time
from datetime import datetime

class FileManager():
    def __init__(self):
        self.path = Path(input('Give a path: '))
    
    def path_validation(self):
        while True:
            if self.path.is_absolute() and self.path.exists() and self.path.is_dir():
                print('It is a valid absolute directory path.')
                break
            else:
                print('Invalid path. Please enter a valid absolute directory path.')
                self.path = Path(input('Give a path: '))

    def versioned(self):
        dic = {}
        for i in self.path.rglob('*'):
            if i.is_file():
                mod_time = i.stat().st_mtime
                dic[i] = mod_time
            

        new_version = self.path / 'Version'
        new_version.mkdir(parents = True, exist_ok=True)
 
        for x in list(dic.keys()):
            time.sleep(5)
            new_mod_time = x.stat().st_mtime
            old_mod = dic[x]
            if old_mod != new_mod_time:
                dt = datetime.fromtimestamp(new_mod_time)
                file_name = x.stem + '_' + dt.strftime('%Y_%m_%d') + x.suffix
                
                shutil.copy2(x, new_version / file_name)
                dic[x] = new_mod_time
                
    def file_manager(self):
        self.path_validation()
        self.versioned()