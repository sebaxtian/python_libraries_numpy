import numpy as np

data = 'somedata.csv'
arr = np.genfromtxt(data, delimiter=',', skip_header=3)   # TODO

if __name__ == '__main__':
    print(arr.shape)
    print(arr.dtype)
    np.savetxt('test.out', arr[:10], delimiter=',')  # Saves the first 10 lines to a new file
