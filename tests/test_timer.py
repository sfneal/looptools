import unittest
from looptools import Timer


class TestTimer(unittest.TestCase):
    @Timer.decorator
    def test_func_timer(self):
        for i in range(0, 100000):
            self.assertEqual(type(i), int)


if __name__ == '__main__':
    unittest.main()
