import numpy as np


def array_from_range(start, stop, step=1):
    return np.arange(start=start, stop=stop, step=step)   # TODO


if __name__ == '__main__':
    up = array_from_range(100, 110)
    down = array_from_range(100, 0, -10)
    print(up)  # Should print '[100 101 102 103 104 105 106 107 108 109]'
    print(down)  # Should print '[100  90  80  70  60  50  40  30  20  10]'
