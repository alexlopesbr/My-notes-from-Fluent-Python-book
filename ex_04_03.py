# 4.03 | 134 | Initializing bytes from raw array data

import array

numbers = array.array('h', [-2, -2, 0, 1, 2])
octets = bytes(numbers)

print(octets)
