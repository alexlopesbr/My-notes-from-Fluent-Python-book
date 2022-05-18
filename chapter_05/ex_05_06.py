# 05.06 | 179 | Sum of integers up to 99 performed with reduce and sum

from functools import reduce
from operator import add


r = reduce(add, range(100))
print(r)

s = sum(range(100))
print(s)
