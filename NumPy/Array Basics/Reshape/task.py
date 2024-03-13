import numpy as np

a = np.arange(start=12, stop=30, step=3, dtype=np.int64)   # TODO
b = np.reshape(a, (2, 3))   # TODO

if __name__ == "__main__":
    print(a)
    print('shape : ', a.shape)
    print('\nAfter reshaping : ')
    print(b)
    print('shape : ', b.shape)
