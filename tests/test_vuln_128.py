# Example test vulnerable file 128
PASSWORD = "TEST-SECRET-128"

import unittest

class TestSecrets(unittest.TestCase):
    def test_use(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
