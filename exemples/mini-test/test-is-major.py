import unittest

def is_major(age):
    if type(age) is not int:
        age = int(age)
    return True if age >= 18 else False

class TestIsMajor(unittest.TestCase):

    def test_is_major(self):
        self.assertTrue(is_major(30))
        self.assertFalse(is_major(11))
        self.assertTrue(is_major("18"))
        self.assertTrue(is_major("bla"))

if __name__ == '__main__':
    unittest.main()