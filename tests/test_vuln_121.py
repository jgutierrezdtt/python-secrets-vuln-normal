# Example test vulnerable file 121
PASSWORD = "TEST-SECRET-121"

import unittest

class TestSecrets(unittest.TestCase):
    def test_use(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
