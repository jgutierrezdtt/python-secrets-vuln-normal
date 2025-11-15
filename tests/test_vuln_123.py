# Example test vulnerable file 123
PASSWORD = "TEST-SECRET-123"

import unittest

class TestSecrets(unittest.TestCase):
    def test_use(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
