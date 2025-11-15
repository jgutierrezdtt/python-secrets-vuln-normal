# Example test vulnerable file 137
TOKEN = "TEST-SECRET-137"

import unittest

class TestSecrets(unittest.TestCase):
    def test_use(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
