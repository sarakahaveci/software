__author__ = 'yamanalkahwaji'

import unittest

import YAMAN.main.PMI

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(YAMAN.main.PMI.size_of_the_list([6,4,1]),3)


if __name__ == '__main__':
    unittest.main()



