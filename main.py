from file_organizer import FileOrganizer
from duplicate_file_finder import DuplicateFilesFinder
from user_info import UserInfo
from versioned_file_manager import FileManager
from backup import Backup

while True:
    choice = input('''
Welcome! Choose an option:
1. File organization
2. Duplicated files analysis
3. Contact book
4. Versional file managing
5. Backup
6. Exit
Enter your choice:
''')

    if choice == '1':
        fo = FileOrganizer()
        fo.organiztion()
        break
        
    elif choice == '2':
        df = DuplicateFilesFinder()
        df.file_finder()
        break
        
    elif choice == '3':
        cb = UserInfo()
        cb.contact_info()
        break
        
    elif choice == '4':
        fm = FileManager()
        fm.file_manager()
        break
        
    elif choice == '5':
        try:
            bk = Backup()
            bk.back_up_process()
        except ValueError as e:
            print(f'Error: {e}')
        break
        
    elif choice == '6':
        print("""
    You didn't choose required option. The program is shutting down.
    Goodbye""")
        break
    
    else:
        print('Invalid choice.\nPlease enter a number from 1 to 6.')
