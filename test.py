import unittest
from unittest.mock import patch
import main

class TestingFunctions(unittest.TestCase):
    @patch('builtins.input', side_effect=['2','0','4'])
    @patch('builtins.print')
    def test_it_works(self, mock_print, mock_input):
        main.main()
        mock_print.assert_called_with('the average is 2.00')

    @patch('builtins.input', side_effect=['e','-1','2','0','4'])
    @patch('builtins.print')
    def testing_except_and_else(self, mock_print, mock_input):
        main.main()
        self.assertIn(
            unittest.mock.call('Please enter a number'),
            mock_print.mock_calls
        )
        self.assertIn(
            unittest.mock.call('Enter a number greater than 0'),
            mock_print.mock_calls
        )
        self.assertIn(
            unittest.mock.call('the average is 2.00'),
            mock_print.mock_calls
        )
    

if __name__ == "__main__":
    unittest.main()