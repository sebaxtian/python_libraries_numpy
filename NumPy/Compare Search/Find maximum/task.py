import numpy as np

data = np.genfromtxt('data.csv', delimiter=',', dtype=np.int64)   # Import data
maxima = np.argmax(data, axis=1)   # Find indices of maximum values in each row
maxima = np.expand_dims(maxima, axis=1)
result = np.take_along_axis(data, maxima, axis=1)   # Extract the maximum elements from each row

if __name__ == '__main__':
    print(result)
