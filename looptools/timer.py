import time


class Timer:
    def __init__(self, msg=None):
        self.msg = msg
        self.start = time.time()
        self.elapsed_str = None
        self.elapsed_float = None

    def __str__(self):
        return str(self.end)

    def __float__(self):
        return float(self.elapsed_float)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.msg:
            print(self.msg, self.end)
        else:
            print(self.end)

    @property
    def end(self):
        end = time.time()
        self.elapsed_float = end - self.start
        if self.elapsed_float < 60:
            self.elapsed_str = str('sec: ' + str(self.elapsed_float))
        else:
            self.elapsed_str = str('min: ' + str(self.elapsed_float/60))
        return self.elapsed_str

    @staticmethod
    def decorator(func):
        """A function timer decorator."""

        def function_timer(*args, **kwargs):
            """A nested function for timing other functions."""
            start = time.time()
            value = func(*args, **kwargs)
            end = time.time()
            runtime = end - start
            msg = '{func:15} --> {time}'
            print(msg.format(func=func.__name__, time=runtime))
            return value

        return function_timer
