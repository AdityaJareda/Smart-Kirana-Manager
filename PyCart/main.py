import constants
import cart
import member

def display_menu():
    print(constants.welcome_msg)

    for key, value in constants.menu_options.items():
        print(f'{key}. {value}')

def run():

    print('------- Login or Register -------\n')
    user_type=member.login()

    if user_type is None:
        print('------- Login Failed! Exiting... -------')
        return

    discount=member.apply_discount(user_type)
    print(f'You are logged in as {user_type.replace("_", " ").title()} and you have a {discount*100}% discount on all items.\n')

    while True:
        display_menu()
        choice=input('Enter your choice: ')

        try:
            choice=int(choice)
            if choice==1:
                for key, value in constants.categories.items():
                    print(f'{key}. {value}')
            elif choice==2:
                print('To remove items')
            elif choice==3:
                print('To view cart')
            elif choice==4:
                print('To checkout')
            elif choice==5:
                print(constants.exit_msg)
                break
            else:
                print('Invalid input entered. Please try again.')
        except (ValueError):
            print('Invalid input entered. Please enter a number.')

if __name__=='__main__':
    run()
