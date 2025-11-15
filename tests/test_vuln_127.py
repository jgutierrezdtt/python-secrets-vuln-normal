# Example test vulnerable file 127
TOKEN = "TEST-SECRET-127"

import unittest

class TestSecrets(unittest.TestCase):
    def test_use(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
