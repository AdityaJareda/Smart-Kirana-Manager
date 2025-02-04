import constants
import os
from getpass import getpass as gp

def load_users():
    users={}
    if os.path.exists(constants.user_file):
        with open(constants.user_file, 'r') as file:
            for line in file:
                username, password, user_type, checkout_count = line.strip().split(',')
                users[username]={
                    "password": password,
                    "user_type": user_type,
                    "checkout_count": int(checkout_count)
                }
    return users

def save_user(users):
    with open(constants.user_file, 'w') as file:
        for username, details in users.items():
            file.write(f"{username},{details['password']},{details['user_type']},{details['checkout_count']}\n")

def save_users(username, password, user_type):
    with open(constants.user_file, 'a') as file:
        file.write(f'{username},{password},{user_type},0\n')


def login():
    users=load_users()

    username=input("Enter username: ")
    password=gp("Enter password: ")

    if username in users:

        if users[username]["password"]==password:
            print(f'\n------- Welcome!!! -------')
            return username, users[username]["user_type"], users[username]['checkout_count']
        else:
            print("Incorrect Username or Password!")
            return None, None, None
        
    else:
        print("You are not a registered user. Would you like to sign up? (yes/no)")
        choice=input().strip().lower()

        if choice=='yes':
            new_user_type="first_time"
            save_users(username, password, new_user_type)
            print("You have been successfully registered as a First-Time user!\n")
            return username, new_user_type, 0
        else:
            print("------- Login cancelled! -------")
            return None, None, None

def apply_discount(user_type):
    if user_type == 'member':
        return constants.member_discount
    elif user_type == 'first_time':
        return constants.first_time_user_discount
    else:
        return constants.guest_discount
    
def update_user_status(username, user_type, checkout_count):
    users=load_users()

    if username in users:
        if user_type=='first_time':
            users[username]['user_type']="guest"
            users[username]['checkout_count'] = 1
            print(f'------- User ^{username}^ is now a Guest. -------')
        
        elif user_type=='guest':
            users[username]['checkout_count'] += 1
            print(f'------- User ^{username}^ total checkout: {users[username]['checkout_count']} -------')

            if users[username]['checkout_count'] >= 5:
                users[username]['user_type']="member"
                users[username]['checkout_count'] = 0
                print('------- You have been upgraded to Member. -------')
        save_user(users)
