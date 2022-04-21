# 02.21 | 79 | Changing the value of an array item by changing one of its bytes
import array

numbers = array.array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)

# print(len(memv))
# print(memv[0])

memv_oct = memv.cast('B')

# print(memv_oct.tolist())

print(numbers)
print(memv_oct[5])
memv_oct[5] = 4
print(numbers)
print(memv_oct[5])
