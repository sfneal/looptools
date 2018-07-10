import time


class Timer:
    def __init__(self):
        self.start = time.time()
        self.elapsed_str = None
        self.elapsed_float = None

    def __str__(self):
        return str(self.elapsed_str)

    def __float__(self):
        return float(self.elapsed_float)

    @property
    def end(self):
        end = time.time()
        self.elapsed_float = end - self.start
        if self.elapsed_float < 60:
            self.elapsed_str = str('sec: ' + str(self.elapsed_float))
        else:
            self.elapsed_str = str('min: ' + str(self.elapsed_float/60))
        return self.elapsed_str