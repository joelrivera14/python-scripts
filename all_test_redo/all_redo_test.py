import unittest
from unittest.mock import patch
import all_redo

class TestAllRedo(unittest.TestCase):
    @patch('builtins.input', side_effect=['2','0','4'])
    @patch('builtins.print')
    def test_main_basic(self,mock_print, mock_input):
        all_redo.main()
        mock_print.assert_called_with('your average is 2.0')
    
    @patch('builtins.input', side_effect=['-1','2','0','6'])
    @patch('builtins.print')
    def test_number_less_than_zero(self, mock_print, mock_input):
        all_redo.main()
        self.assertIn(
            unittest.mock.call('The integer should be greater than 0'),
            mock_print.mock_calls
        )
        self.assertIn(
            unittest.mock.call('your average is 3.0'),
            mock_print.mock_calls
        )
    
    @patch('builtins.input', side_effect=['2','e','0','8'])
    @patch('builtins.print')
    def test_letter_input(self,mock_print,mock_input):
        all_redo.main()
        self.assertIn(
            unittest.mock.call('Doesnt accept non-integer values'),
            mock_print.mock_calls
        )
        self.assertIn(
            unittest.mock.call('your average is 4.0'),
            mock_print.mock_calls
        )
    
    def test_rearrange_basic(self):
        testName='Joel, Rivera'
        expected ='Rivera, Joel'
        self.assertEqual(all_redo.rearrange_name(testName), expected)
    
    def test_empty_string(self):
        testName = ""
        expected = ""
        self.assertEqual(all_redo.rearrange_name(testName),expected)
    
    def test_one_name(self):
        testName='Joel'
        expected='Joel'
        self.assertEqual(all_redo.rearrange_name(testName), expected)

if __name__ == '__main__':
    unittest.main()