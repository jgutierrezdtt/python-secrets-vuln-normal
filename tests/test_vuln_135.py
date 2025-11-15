# Example test vulnerable file 135
API_KEY = "TEST-SECRET-135"

import unittest

class TestSecrets(unittest.TestCase):
    def test_use(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
