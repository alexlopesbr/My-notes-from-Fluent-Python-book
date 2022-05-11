# 2.6 | 51 | Cartesian product in a generating expression

colors = ['black', 'white']
sizes = ['S', 'M', 'L']

for tshirt in (f'{c} - {s}' for c in colors for s in sizes):
    print(tshirt)
