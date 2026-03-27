import unittest
from validate import validate_user

class TestValidate(unittest.TestCase):
    def test_basic(self):
        name = 'joel'
        minLen = 3
        expected = True
        self.assertEqual(validate_user(name, minLen), expected)
    
    def test_special_chars(self):
        name = "**(()(&^%$@@!))"
        minLen = 5
        expected = False
        self.assertEqual(validate_user(name, minLen), expected)
    
    def test_not_enough_chars(self):
        name = 'Joel'
        minLen = 5
        expected = False
        self.assertEqual(validate_user(name, minLen), expected)

if __name__ == "__main__":
    unittest.main()