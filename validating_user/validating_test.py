import unittest
from validate import validate_user

class TestValidate(unittest.TestCase):
    def test_basic(self):
        name = 'joel'
        minLen = 10
        expected = False
        self.assertEqual(validate_user(name, minLen), expected)

if __name__ == "__main__":
    unittest.main()