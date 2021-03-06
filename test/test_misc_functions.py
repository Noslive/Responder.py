import unittest
from mock import patch
import sys

import os
from gladius import find_file

class TestFindFile(unittest.TestCase):
    @patch("gladius.os")
    def test_find_file(self, mock_os):
        mock_os.walk.return_value = [('root', ['dir1', 'dir2'], ['f1', 'f2'])]

        filepath = find_file('f2')

        mock_os.path.join.assert_called_with('root', 'f2')

if __name__ == '__main__':
    unittest.main()
