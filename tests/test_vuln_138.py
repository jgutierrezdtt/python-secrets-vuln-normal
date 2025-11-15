# Example test vulnerable file 138
PRIVATE_KEY = "TEST-SECRET-138"

import unittest

class TestSecrets(unittest.TestCase):
    def test_use(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
