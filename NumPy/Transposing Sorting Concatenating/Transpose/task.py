import numpy as np

a = np.array([['clear', 'usually', 'of'],
              ['conscience', 'the', 'bad'],
              ['is', 'sign', 'memory']])
# TODO
a = a.T

b = np.array([[0, 3, 6], [1, 4, 7], [2, 5, 8]])
# TODO
b = b.transpose()

c = np.arange(12).reshape(3, 2, 2).T   # TODO


if __name__ == '__main__':
    print(a)
    print(b)
    print(c)

