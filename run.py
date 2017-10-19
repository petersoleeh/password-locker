#!/usr/bin/env python3.6
import getpass
from password import User, Credentials


def create_user(user_name, password):
    new_user = User(user_name, password)
    return new_user


def save_users(user):
    user.save_user()


def find_user(name):
    return User.find_by_name(name)


def check_user_exists(user_name, password):
    if_user_exist = Credentials.user_exist(user_name,password)
    return if_user_exist

def create_credential(account_name,account_password):
    new_credential = Credentials(account_name,account_password)

    return new_credential

def save_credential(credential):
    credential.save_account()

def display_accounts(credential):
    return Credentials.display_accounts()



def main():
    print("The password Locker")
    print('\n')

    while True:
        print("Do you want to Login(l) or Signup(s)? l/s?..To Quit press (q) ")

        code = input().strip()
        if code == "q":
            print("Bye....")
            break
        elif code == 's':
            print("NEW USER")
            print('\n')

            username = input("Username: ")
            password = getpass.getpass("Password: ")

            save_users(create_user(username, password))
            print('\n')

            print(f"Signup successful new user {username} has been created")

        elif code == 'l':
            print("Fill in your credentials to login")
            print('\n')

            user_name = input("Username: ")
            password = getpass.getpass("Password: ")
            log_in = check_user_exists(user_name,password)
            if log_in == True:
                print(f"Welcome back {user_name},how can i help you?")
                while True:
                    print('.'*30)
                    print("Create account - ca- ,Display accounts -da - ,Quit - q ")

                    code = input().strip()
                    print('.'*30)

                    if code == "q":
                        print("Bye ............")
                        break

                    elif code == "ca":
                        print("Creating New Account Credentials")
                        print('\n')
                        account_name = input("Account Name: ")



            break


if __name__ == '__main__':
    main()
