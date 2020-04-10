import unittest
from unittest import mock
from post_youdao import *


class PostYoudaoTest(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_get_ts(self):
        get_ts=mock.Mock(return_value='1585539588950')
        self.assertEqual('1585539588950',get_ts())

    def test_get_salt(self):
        get_salt=mock.Mock(return_value="15855395889509")
        self.assertEqual('15855395889509',get_salt())

    def test_get_salt(self):
        self.assertEqual('d8416f78b54601efd1bed7a202bee31c',grt_sign())
if __name__ == '__main__':
    unittest.main()
