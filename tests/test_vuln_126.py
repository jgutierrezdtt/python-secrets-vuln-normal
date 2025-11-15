# Example test vulnerable file 126
PRIVATE_KEY = "TEST-SECRET-126"

import unittest

class TestSecrets(unittest.TestCase):
    def test_use(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
