# 04.02 | 132 | A sequence of five bytes in bytes and as bytearray

cafe = bytes('café', encoding='utf-8')
print(cafe)
print(cafe[0])
print(cafe[:1])

cafe_arr = bytearray(cafe)
print(cafe_arr)
print(cafe_arr[-1:])
