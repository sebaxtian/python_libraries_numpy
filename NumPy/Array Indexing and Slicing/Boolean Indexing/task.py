import numpy as np

a = np.arange(20).reshape((2, 2, 5))   # TODO
mask = np.array([[True, False], [False, True]])   # TODO
c = a[mask]

if __name__ == '__main__':
    print('Array a:\n', a, '\n')
    print('Indexed array c:\n', c)
    print(c.shape)
