import unittest

class TestIsEvenMethod(unittest.TestCase):
    def test_isEven(self):
        x = 6
        self.assertTrue(isEven(x))
        self.assertEqual(1,isEven(x))

    def test_isEven3(self):
        with self.assertRaises(TypeError):
            isEven('hello')


def isEven(val):
    if val % 2 == 0:
        return 1
    else:
        return 0




if __name__ == '__main__':
    unittest.main()
