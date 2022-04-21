# 2.5 | 51 | initializing a tuple and an array from a generator expression

import array

symbols = '$¢£¥€¤'

symbols_position_tuples = tuple(ord(symbol) for symbol in symbols)

print(symbols_position_tuples)

# =========================

symbols_position_array = array.array('I', (ord(symbol) for symbol in symbols))

print(symbols_position_array)
