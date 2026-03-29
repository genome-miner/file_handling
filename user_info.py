import shelve

class UserInfo:
    def __init__(self):
        self.user_info = 'user_content'
        
    def contact_info(self):
        with shelve.open(self.user_info) as info:
            while True:
                menu_options = input('What do you want to choose first:\n Add\n View\n Update\n Delete\n Exit\n').strip().lower()
  
                if menu_options == 'add':
                    name = input('Enter your name: ').strip().title()
                    phone = input('Enter your phone number: ')
                    email = input('Enter your email: ')
                    info[name] = {'phone': phone, 'email': email}
                    print(f'Contact "{name}" added successfully.')
                    
                elif menu_options == 'view':
                    if len(info) == 0:
                        print('No contact found.')
                    else:
                        for name, values in info.items():
                            print(f'Name: {name}')
                            print(f"Phone: {values['phone']}") 
                            print(f"Email: {values['email']}")
                            print('---------------------------')
                            
                elif menu_options == 'update':
                    contact_name = input('Enter contact name which you want to update: ').strip().title()
                    
                    if contact_name not in info:
                        print('Contact not found.')
                    else:
                        values = info[contact_name]
                        print(f"Current Phone: {values['phone']}")
                        print(f"Current Email: {values['email']}")
                        
                        new_email = input('Enter your new email: ').strip()
                        values['email'] = new_email
                        
                        new_number = input('Enter your new number: ').strip()
                        values['phone'] = new_number
                        
                        info[contact_name] = values
                        print('Contact updated successfully.')
                        
                elif menu_options == 'delete':
                    contact_name = input(
                        'Enter contact name which you want to delete: '
                    ).strip().title()
                    
                    if contact_name not in info:
                        print('Contact not found.')
                    else:
                        confirmation = input('Are you sure you want to delete, Yes or No: ').strip().lower()
                        
                        if confirmation == 'yes':
                            del info[contact_name]
                            print('Contact deleted successfully.')
                        elif confirmation == 'no':
                            print('Deletion cancelled.')
                        else:
                            print('Invalid input. Please enter Yes or No.')
                            
                elif menu_options == 'exit':
                    print('Exiting from the program. Goodbye')
                    break
                
                else:
                    print('Invalid option. Please choose Add, View, Update, Delete, or Exit.')