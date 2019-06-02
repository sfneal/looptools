import unittest
from looptools import Timer
from time import sleep


class TestTimer(unittest.TestCase):
    @Timer.decorator
    def test_mms(self):
        sleep(.05)

    @Timer.decorator
    def test_sec(self):
        sleep(1.1)


if __name__ == '__main__':
    unittest.main()
