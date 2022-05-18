# 05.05 | 178 | Factor list generated with map and filter,
# compared to alternatives written with listcomps

from ex_05_01 import factorial
from ex_05_02 import fact


list_map = list(map(fact, range(6)))
print(list_map)

list_comp = [fact(x) for x in range(6)]
print(list_comp)

list_map_2 = list(map(factorial, filter(lambda n: n % 2, range(6))))
print(list_map_2)

list_comp_2 = [factorial(x) for x in range(6) if x % 2]
print(list_comp_2)
