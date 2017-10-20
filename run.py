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

def display_accounts():
    return Credentials.display_accounts()

def password_generator():
    new_pass = Credentials.generate_password()
    return new_pass




def main():
    print("The password Locker")
    print('\n')

    while True:
        print("Do you want to Login(l) or Signup(s)? l/s?..To Quit press (q) ")

        code = input().lower().strip()
        if code == "q":
            print("Bye...0_0")
            break
        elif code == 's':
            print("NEW USER")
            print('\n')

            username = input("Username: ")
            password = getpass.getpass("Password: ")

            save_users(create_user(username, password))
            print('\n')

            print(f"Signup successful new user {username} has been created")
            print('.'*60)

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
                    print("Create account - ca- ,Display accounts -da - ,Press - q - to go to the top Menu ")

                    code = input().lower().strip()
                    print('.'*30)

                    if code == "q":
                        print("Bye...0_0")
                        break

                    elif code == "ca":
                        print("Creating New Account Credentials")
                        print('\n')
                        account_name = input("Account Name: ")
                        print('.'*30)
                        while True:
                            print("Generate new account password -np- , Enter existing password - ep -")
                            code = input().strip()

                            if code == "ep":
                                account_password = input("Account Password: ")
                                # save_credential(create_credential(account_name,account_password))

                                # print('\n')
                                # print(f"Existing credential are as follows: \n Account Name:  {account_name} \n password: {account_password} ")
                                # print('\n')
                                break

                            elif code =="np":
                                account_password = password_generator()
                                break

                            else:
                                print('.'*30)
                                print("please enter valid shortcode ")
                                break
                        save_credential(create_credential(account_name,account_password))

                        print('\n')
                        print(f"New account credential created: \n Account Name:  {account_name} \n password: {account_password} ")
                        print('\n')


                    elif code == "da":
                        if display_accounts():
                            print("Here is a list of your accounts credentials")
                            print('\n')

                            for account in display_accounts():
                                print(f" \nAccount Name: {account.account_name}  \nAccount Password: {account_password}")
                                print('\n')

                        else:
                            print('\n')
                            print("No saved accounts credentials yet")
                            print('\n')

            else:
                print('\n')
                print("User NOT FOUND!!. Please Signup")
                print('.'*60)
        else:
            print("INVALID ENTRY. PLEASE ENTER VALID SHORT CODES")
            print('.'*60)








if __name__ == '__main__':
    main()
