import unittest
from unittest.mock import patch
import all

class TestAll(unittest.TestCase):
    @patch('builtins.input', side_effect=['2'])
    @patch('builtins.print')
    def test_main_basic(self, mock_print, mock_input):
        all.main()
        mock_print.assert_called_with(2)
    
    @patch('builtins.input', side_effect=['-1', 'e','5'])
    @patch('builtins.print')
    def test_edge_cases(self, mock_print, mock_input):
        all.main()
        self.assertIn(
            unittest.mock.call(f'must be greater than zero'),
            mock_print.mock_calls
        )
        self.assertIn(
            unittest.mock.call(f'must be a number'),
            mock_print.mock_calls
        )
        mock_print.assert_called_with(5)
    
    def test_rearrange_basic(self):
        testName='Joel, Rivera'
        expected='Rivera, Joel'
        self.assertEqual(all.rearrange(testName), expected)
    
    def test_one_name(self):
        testName='Joel'
        expected='Joel'
        self.assertEqual(all.rearrange(testName), expected)

if __name__ == '__main__':
    unittest.main()
    