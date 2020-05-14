import unittest
import sansu

class MyTestCase(unittest.TestCase):
    def test_add_num(self):
        self.assertEqual(10, sansu.add_num(6, 4))

    def test_sub_num(self):
        self.assertEqual(2, sansu.sub_num(6, 4))

    def test_mul_num(self):
        self.assertEqual(24, sansu.mul_num(6, 4))

    def test_div_num(self):
        self.assertEqual(10, sansu.div_num(6, 4))


if __name__ == '__main__':
    unittest.main()
