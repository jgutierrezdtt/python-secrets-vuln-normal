# Example test vulnerable file 132
PASSWORD = "TEST-SECRET-132"

import unittest

class TestSecrets(unittest.TestCase):
    def test_use(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
