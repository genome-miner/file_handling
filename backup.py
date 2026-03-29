from pathlib import Path
import datetime
import zipfile
import os
import sys

class Backup():
    def __init__(self):
        self.src_path = Path(input('Give a source path: '))
        self.dis_path = Path(input('Give a destination path: '))

        # Source path validation
        if not (self.src_path.exists() and self.src_path.is_dir()):
            raise ValueError(f'Source path is not valid: {self.src_path}')
    
        # Destination path validation
        if not (self.dis_path.exists() and self.dis_path.is_dir()):
            raise ValueError(f'Destination path is not valid: {self.dis_path}')
    
        # Current time
        current_time = datetime.datetime.now()
        self.zip_file = 'backup_' + current_time.strftime('%y_%m_%d') + '.zip'

    def back_up_process(self):
        backup_path = self.dis_path / self.zip_file

        if backup_path.exists():
            # Append mode
            with zipfile.ZipFile(backup_path, mode='a') as zf:
                existing_files = zf.namelist()
                for folder, subfolders, files_name in os.walk(self.src_path):
                    for file in files_name:
                        file_path = os.path.join(folder, file)
                        relative_path = os.path.relpath(file_path, self.src_path)
                        if relative_path not in existing_files:
                            zf.write(
                                file_path,
                                arcname=relative_path,
                                compress_type=zipfile.ZIP_DEFLATED,
                                compresslevel=9)
                            
                        else:
                            print(f'{relative_path} already present')
        else:
            # Create new zip
            with zipfile.ZipFile(backup_path, mode='w') as zf:
                for folder, subfolders, files_name in os.walk(self.src_path):
                    for file in files_name:
                        file_path = os.path.join(folder, file)
                        relative_path = os.path.relpath(file_path, self.src_path)
                        zf.write(
                            file_path,
                            arcname=relative_path,
                            compress_type=zipfile.ZIP_DEFLATED,
                            compresslevel=9)

        print(f'Backup completed: {backup_path}')
