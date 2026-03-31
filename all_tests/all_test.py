import unittest
from unittest.mock import patch
import all

class TestAll(unittest.TestCase):
    @patch('builtins.input', side_effect = ['2'])
    @patch('builtins.print')
    def test_printValue_basic(self, mock_print, mock_input):
        all.printValue()
        mock_print.assert_called_with(2)
    
    @patch('builtins.input',side_effect=['-1','e','1'])
    @patch('builtins.print')
    def test_printValue_edge_cases(self,mock_print,mock_input):
        all.printValue()
        self.assertIn(
            unittest.mock.call('number greater than 0'),
            mock_print.mock_calls
        )
        self.assertIn(
            unittest.mock.call('enter a number'),
            mock_print.mock_calls
        )
        mock_print.assert_called_with(1)

    def test_rearrange_basic(self):
        testN='Joel, Rivera'
        e='Rivera, Joel'
        self.assertEqual(all.rearrange(testN), e)

if __name__ == '__main__':
    unittest.main()
