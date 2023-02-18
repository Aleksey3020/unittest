import unittest
from triangle import Triangle


class TestTriangleUnit(unittest.TestCase):

    def setUp(self):
        self.first = Triangle(4, 4, 5)

    def tearDown(self):
        del self.first

    def test_triangle_perimetr(self):
        self.assertEqual(self.first.perimetr(), 13)

    def test_triangle_perimetr1(self):
        self.second = Triangle(9, 7, 6)
        self.assertEqual(self.second.perimetr(), 22)

    def test_square(self):
        self.second = Triangle(3, 4, 5)
        self.assertEqual(self.second.square(), 6)

    def test_triangle_eq(self):
        second = Triangle(4, 4, 5)
        self.assertEqual(self.first, second)

    def test_triangle_ne(self):
        second = Triangle(5, 4, 5)
        self.assertNotEqual(self.first, second)

    def test_triangle_lt(self):
        second = Triangle(6, 4, 5)
        self.assertLess(self.first.perimetr(), second.perimetr())

    def test_triangle_gt(self):
        second = Triangle(3, 4, 4)
        self.assertGreater(self.first.perimetr(), second.perimetr())

    def test_triangle_le(self):
        second = Triangle(6, 4, 5)
        self.assertLessEqual(self.first.perimetr(), second.perimetr())

    def test_triangle_ge(self):
        second = Triangle(4, 4, 5)
        self.assertGreaterEqual(self.first.perimetr(), second.perimetr())

    def test_triangle_corners(self):
        second = Triangle(8, 8, 10)
        self.assertTrue(self.first.with_same_corners(second))

    def test_right_angled(self):
        second = Triangle(3, 4, 5)
        self.assertTrue(second.is_right_angled())

    @unittest.skip('bug in function')
    def test_right_angled1(self):
        second = Triangle(5, 4, 3)
        self.assertTrue(second.is_right_angled())

    def test_equilateral_triangle(self):
        second = Triangle(4, 4, 4)
        self.assertTrue(second.is_right_triangle())

    def test_isosceles_triangle(self):
        self.assertTrue(self.first.two_sides_eq())


if __name__ == '__main__':
    unittest.main()
