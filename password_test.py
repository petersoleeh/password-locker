import unittest
from password import User


class TestUser(unittest.TestCase):
    def setUp(self):
        '''
        test setup method
        '''
        self.new_user = User("Peter", "Welcome123")

    def test_init(self):
        '''
        test initialization
        '''
        self.assertEqual(self.new_user.user_name, "Peter")
        self.assertEqual(self.new_user.password, "Welcome123")

    def test_save_user(self):
        '''
        see if the user is saved
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

    def tearDown(self):
        User.user_list = []

    def test_save_multiple_user(self):
        '''
        test if multiple users will be saved
        '''
        self.new_user.save_user()

        test_user = User("Josie", "123456")
        test_user.save_user()

        self.assertEqual(len(User.user_list), 2)

    def test_login(self):
        '''
        test login by inputting user name and password
        '''
        self.new_user.save_user()

        test_user = User("Josie", "123456")
        test_user.save_user()

        user_exists = User.user_exist("Josie")
        self.assertTrue(user_exists)

    def test_find_user(self):
        '''
        test to check for a specific user using their name
        '''
        self.new_user.save_user()

        test_user = User("Josie", "123456")
        test_user.save_user()

        user_found = User.find_by_name("Josie")
        self.assertEqual(user_found.password, test_user.password)


if __name__ == '__main__':
    unittest.main(verbosity=2)
