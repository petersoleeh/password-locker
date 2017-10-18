#!/usr/bin/env python3.6
import string
import random

global user_list
class User:
    """docstring for User."""

    user_list = []

    def __init__(self, user_name, password):
        '''
        class properties
        '''

        self.user_name = user_name
        self.password = password

    def save_user(self):
        '''
        save user_list
        '''
        User.user_list.append(self)

    @classmethod
    def find_by_name(cls, name):
        for user in cls.user_list:
            if user.user_name == name:
                return user


class Credentials:

    '''
    instanciate credential
    '''

    global user_list
    credential_list =[]

    def __init__(self, account_name,account_password):
        self.account_name = account_name
        self.account_password = account_password

    def save_account(self):

        """
        save to credential_list
        """
        Credentials.credential_list.append(self)



    @classmethod
    def user_exist(cls, user_name,password):
        '''
        check whether current user exist and login
        '''
        for user in cls.user_list:
            if user.user_name == user_name and user.password == password:
                return True
        return False


    @classmethod
    def display_accounts(cls):

        """
        display items in the credential list
        """
        return cls.credential_list
