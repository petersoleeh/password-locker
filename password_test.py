import unittest
from password import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("Peter", "Welcome123")

    def test_init(self):
        self.assertEqual(self.new_user.user_name, "Peter")
        self.assertEqual(self.new_user.password, "Welcome123")


if __name__ == '__main__':
    unittest.main(verbosity=2)
