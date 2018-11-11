#define contact phone book
#def menu

from os import path

phone_book_name = 'Runa Phone Book.txt'

def print_menu():
    print(40*'-')
    print(16*' ','MENU', 16*' ')
    print(40*'-')
    print('1. Show Phone Book')
    print('2. Add new contact')
    print('3. Exit')
    print(40*'-')

def show_phone_book():
    if not path.exists(phone_book_name):
        print('\nfile not exist')
        return
    with open(phone_book_name, 'r') as f:
        file_content = f.readlines()
    for line in file_content:
        entry = line.split(';')
        print(40*'*')
        print(('First Name is {}').format(entry[0]))
        print(('Last Name is {}').format(entry[1]))
        print(('Phone Number is {}').format(entry[2]))
        print(40*'*')


def add_new_entry():
    first_name = input('Please input your first name:\n')
    last_name = input('Please input your last name:\n')
    phone_number = input('Please input your phone number:\n')
    #print('New entry added: {}; {}; {}'.format(first_name, last_name, phone_number))
    new_entry = '{}; {}; {}\n'.format(first_name, last_name, phone_number)
    with open(phone_book_name, 'a') as f:
        f.write(new_entry)

def start_menu():
    user_option = None
    while (user_option != '3'):
        print_menu()
        user_option = input('select the number [1-3]:')
        if user_option == '1':
            show_phone_book()
        elif user_option == '2':
            add_new_entry()
        elif user_option =='3':
            return
        else:
            print('\nYour input is invalid')

start_menu()      
