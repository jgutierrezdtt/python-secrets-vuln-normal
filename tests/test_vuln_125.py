# Example test vulnerable file 125
TOKEN = "TEST-SECRET-125"

import unittest

class TestSecrets(unittest.TestCase):
    def test_use(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
