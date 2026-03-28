import unittest
from rearrange import rearrange_name

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testCase = 'Joel, Rivera'
        expected = 'Rivera Joel'
        self.assertEqual(rearrange_name(testCase), expected)
    
    def test_empty(self):
        testCase = ''
        expected = ''
        self.assertEqual(rearrange_name(testCase), expected)
    
    def test_double_name(self):
        testCase = 'Joel, Rivera O.'
        expected = 'Rivera O. Joel'
        self.assertEqual(rearrange_name(testCase), expected)
    
    def test_one_name(self):
        testCase = 'Joel'
        expected = 'Joel'
        self.assertEqual(rearrange_name(testCase), expected)

if __name__ == "__main__":
    unittest.main()