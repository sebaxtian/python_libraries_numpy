import numpy as np


a = np.zeros((3, 4), dtype=np.int64)
b = np.arange(4).reshape(1, 4)   # TODO
c = np.concatenate((a, b), axis=0)   # TODO

stacked = np.vstack((np.arange(10), np.arange(20, 30), np.arange(40, 50)))   # TODO

if __name__ == '__main__':
    print(c)
    print(stacked)
