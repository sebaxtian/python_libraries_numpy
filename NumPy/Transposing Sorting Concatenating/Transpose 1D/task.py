import numpy as np


def reshape_transpose(start, stop, step=1):
    # Create a 1D array using arange function
    x = np.arange(start, stop, step)
    # Reshape the 1D array so that you can transpose it
    x = x.reshape(1, x.shape[0])
    return x.T   # Return the transposed array


if __name__ == '__main__':
    print(reshape_transpose(1, 100, 10))
    print(reshape_transpose(0, 5))
