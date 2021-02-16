# Author:  Aaron Nesbit
# Date:    2/15/2021
# Course:  CS362-400-W2021
# Program: Activity 2 - TDD

import unittest
from check_pwd import check_pwd


class MyTestCase(unittest.TestCase):
    def test1(self):
        # This test verifies if an empty string is rejected correctly
        self.assertFalse(check_pwd(""))

    def test2(self):
        # This test verifies that password over 20 characters long is rejected
        self.assertFalse(check_pwd("Abcdefghij0123456789!"))

    def test3(self):
        # This test verifies that password without at least 1 lowercase letter
        # is rejected
        self.assertFalse(check_pwd("ABCD123!"))

    def test4(self):
        # This test verifies that password without at least 1 uppercase letter
        # is rejected
        self.assertFalse(check_pwd("abcd123!"))

    def test5(self):
        # This test verifies that password without at least one digit is
        # rejected
        self.assertFalse(check_pwd("Abcdefg!"))

    def test6(self):
        # This test verifies that password without at least one of the
        # permitted symbols is rejected
        self.assertFalse(check_pwd("Abcd1234"))


if __name__ == '__main__':
    unittest.main()
