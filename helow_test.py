import unittest
from helow import helow

class TestHelow(unittest.TestCase):

    def test_helow(self):
        expected = "helow, helow"
        res = helow("helow")
        self.assertEqual(expected, res)

if __name__ == "__main__":
    unittest.main()

