# 2.10 | 57 | Attributes and methods of a named tuple II

from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')

print('fields', City._fields, '\n')

LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)

print(delhi._asdict(), '\n')

for key, value in delhi._asdict().items():
    print(key + ':', value)


print('\n ======= tests =======')

Fruit = namedtuple('Fruit', 'name price type_fruit')
type_fruit = namedtuple('type_fruit', 'species size')

mango_data = Fruit('Mango', 10, type_fruit('Espada', 'large'))

mango = Fruit._make(mango_data)

print(mango._asdict(), '\n')

print('mango.name', mango.name)
print('mango.price', mango.price)
print('mango.type_fruit.species', mango.type_fruit.species)
print('mango.type_fruit.size', mango.type_fruit.size)
