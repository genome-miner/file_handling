from pathlib import Path
import hashlib
import send2trash

class DuplicateFilesFinder():
    def __init__(self):
        self.path = Path(input('Give a path: '))
        
        while True:
            if self.path.is_absolute() and self.path.exists() and self.path.is_dir():
                print('It is a valid absolute directory path.')
                break
            else:
                print('Invalid path. Please enter a valid absolute directory path.')
                self.path = Path(input('Give a path: '))
 
    def path_scanning(self):
        self.size_record = {}

        for i in self.path.rglob('*'):
            if i.is_file():
                size = i.stat().st_size
            
                if size in self.size_record:
                    self.size_record[size].append(i)
                else:
                    self.size_record[size] = [i]

        print(self.size_record)

    def files_filtering(self):
        for x in list(self.size_record.keys()):
            key_length = len(self.size_record[x])
            
            if key_length > 1:
                print(f'The {x} key has {key_length}.')
            else:
                del self.size_record[x]
    
    def hashing(self):
        hash_dir = {}
        for value in self.size_record.values():
            for file in value:
                with open(file, mode = 'rb') as f:
                    file_content = f.read()
                
                hash_data = hashlib.sha256(file_content)
                hash_key = hash_data.hexdigest()
                if hash_key in hash_dir:
                    hash_dir[hash_key].append(file)
                else:
                    hash_dir[hash_key] = [file]
                    
        for y in hash_dir.values():
            if len(y) > 1:  # Only consider true duplicates
                print("Duplicate files:")
                for index, value in enumerate(y):
                    print(f"Index {index + 1}: {value}")  # Show 1-based index for user

                # Ask user which files to delete (can enter multiple numbers separated by commas)
                file_input = input("Enter the numbers of the files you want to delete, separated by commas (or press Enter to skip): ")

                if file_input.strip() == "":
                    print("Skipping this group.")
                    continue

                # Process user input
                list_str = file_input.split(',')
                for item in list_str:
                    try:
                        integer_in_list = int(item.strip())
                        position = integer_in_list - 1  # Convert to 0-based index
                        if 0 <= position < len(y):
                            send2trash.send2trash(y[position])
                            print(f"Deleted: {y[position]}")
                        else:
                            print(f"Index {integer_in_list} is out of range.")
                    except ValueError:
                        print(f"Invalid input: {item}. Skipping.")
            else:
                print(f"No duplicates in group: {y}")
                
    def file_finder(self):
        self.path_scanning()
        self.files_filtering()
        self.hashing()