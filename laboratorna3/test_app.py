import unittest
from random import choice, randint

from app import Figure

class TestFigure(unittest.TestCase):
    def setUp(self) -> None:
        self.figure = choice(Figure.FIGURES)
        self.length = randint(1, 10)
        self.obj = Figure(self.figure, self.length)

    def tearDown(self) -> None:
        del self.obj

    def test_figure_type(self):
        self.assertEqual(self.figure, self.obj.get_figure_type)

    def test_figure_length(self):
        self.assertEqual(self.length, self.obj.get_figure_length)
    
    def test_obj(self):
        with self.assertRaises(AssertionError):
            Figure("circle", 1)

if __name__ == '__main__':
    unittest.main()
def test_get_angles():
    fig = "triangle"
    triangle = Figure(fig, 1)
    assert triangle.get_angles == 3
