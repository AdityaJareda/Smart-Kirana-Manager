import constants
import os
from getpass import getpass as gp

def load_users():
    users={}
    if os.path.exists(constants.user_file):
        with open(constants.user_file, 'r') as file:
            for line in file:
                username, password, user_type=line.strip().split(',')
                users[username]={'password': password, 'user_type': user_type}
    return users

def save_users(username, password, user_type):
    with open(constants.user_file, 'a') as file:
        file.write(f'{username}, {password}, {user_type}\n')


def login():
    users=load_users()

    username=input("Enter username: ")
    password=gp("Enter password: ")

    if username in users:

        if users[username]['password']==password:
            print(f'\n------- Welcome!!! -------')
            return users[username]['user_type']
        else:
            print("Incorrect Username or Password!")
            return None
        
    else:
        print("You are not a registered user. Would you like to sign up? (yes/no)")
        choice=input().strip().lower()

        if choice=='yes':
            new_user_type="first_time"
            save_users(username, password, new_user_type)
            print("You have been successfully registered as a First-Time user!\n")
            return new_user_type
        else:
            print("------- Login cancelled! -------")
            return None

def apply_discount(user_type):
    if user_type == 'member':
        return constants.member_discount
    elif user_type == 'new_user':
        return constants.first_time_user_discount
    else:
        return constants.guest_discount