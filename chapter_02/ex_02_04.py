# 2.4 | 49 | Cartesian product using a list comprehension
colors = ['black', 'white']
sizes = ['S', 'M', 'L']

tshirts_by_color = [(color, size) for color in colors
                                  for size in sizes]

tshirts_by_size = [(size, color) for size in sizes
                                 for color in colors]


print('by color =>', tshirts_by_color)
print('by size =>', tshirts_by_size)
