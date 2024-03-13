import numpy as np

arr = np.arange(1000)
filter_ = arr % 4 == 0   # TODO: create a boolean array
filtered_arr = arr[np.array(filter_)]   # TODO: use it as a filter/mask


if __name__ == '__main__':
    print(filtered_arr)
