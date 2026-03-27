import unittest
from unittest.mock import patch
from rearrange import rearrange_name

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testCase = 'Joel, Rivera'
        expected = 'Rivera Joel'
        self.assertEqual(rearrange_name(testCase), expected)
    
if __name__ == "__main__":
    unittest.main()
    