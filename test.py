import unittest
from unittest.mock import patch
import main

class Tests(unittest.TestCase):
    @patch('builtins.input', side_effect=['2','0','4'])
    @patch('builtins.print')
    def test_normal_run(self, mock_print, mock_input):
        main.main()
        mock_print.assert_called_with(f'the average is 2.00')
    
    @patch('builtins.input', side_effect=['r','6','1','2','3','4','5','6'])
    @patch('builtins.print')
    def test_first_value_error(self, mock_print, mock_input):
        main.main()
        self.assertIn(
            unittest.mock.call("Please enter a number"),
            mock_print.mock_calls
        )
        self.assertIn(
            unittest.mock.call('the average is 3.50'),
            mock_print.mock_calls
        )
    
    @patch('builtins.input', side_effect=['2','e', '0', '4'])
    @patch('builtins.print')
    def test_second_value_error(self, mock_print, mock_input):
        main.main()
        self.assertIn(
            unittest.mock.call('Enter a number'),
            mock_print.mock_calls
        )
        self.assertIn(
            unittest.mock.call('the average is 2.00'),
            mock_print.mock_calls
        )

if __name__ == '__main__':
    unittest.main()