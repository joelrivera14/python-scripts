import unittest
from unittest.mock import patch
import main

class TestingFunctions(unittest.TestCase):
    @patch('builtins.input', side_effect=['2','0','4'])
    @patch('builtins.print')
    def test_it_works(self, mock_print, mock_input):
        main.main()
        mock_print.assert_called_with('the average is 2.00')

if __name__ == "__main__":
    unittest.main()