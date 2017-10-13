#!/usr/bin/env python3.6
from password import User


def create_user(uname, pword):
    new_user = User(uname, pword)
    return new_user


def main():
    print("The password Locker")
    print('\n')

    while True:
        print("Do you want to Login(l) or Signup(s)? l/s?..To Quit press (q) ")

        break


if __name__ == '__main__':
    main()
