import numpy as np
from numpy import pi
# matplotlib is library for plotting data. We will be discussing it later in detail.
import matplotlib.pyplot as plt


def sine_array(start, stop, num):
    x = np.linspace(start, stop, num)   # TODO
    f = np.sin(x)   # TODO
    return x, f


if __name__ == '__main__':
    a, b = sine_array(0, 3 * pi, 100)
    print(a)
    print(b)

    plt.plot(a, b)
    plt.suptitle('sin(x)')
    plt.show()
