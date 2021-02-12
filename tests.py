# Author:  Aaron Nesbit
# Date:    2/12/2021
# Course:  CS362-400-W2021
# Program: Activity 2 - TDD

import unittest
from check_pwd import check_pwd


class MyTestCase(unittest.TestCase):
    def test1(self):
        # This test verifies if an empty string is rejected correctly
        self.assertFalse(check_pwd(""))


if __name__ == '__main__':
    unittest.main()
