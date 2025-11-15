# Example test vulnerable file 133
API_KEY = "TEST-SECRET-133"

import unittest

class TestSecrets(unittest.TestCase):
    def test_use(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
