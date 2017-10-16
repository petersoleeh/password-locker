#!/usr/bin/env python3.6
import getpass
from password import User


def create_user(uname, pword):
    new_user = User(uname, pword)
    return new_user


def save_users(user):
    user.save_user()


def find_user(name):
    return User.find_by_name(name)


def check_user_exists(name, password):
    return User.user_exist(name)


def main():
    print("The password Locker")
    print('\n')

    while True:
        print("Do you want to Login(l) or Signup(s)? l/s?..To Quit press (q) ")

        code = input().strip()
        if code == 's':
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

            username = input("Username: ")
            password = getpass.getpass("Password: ")

                break


if __name__ == '__main__':
    main()
