# 2.7 | 52 | Tuples used as record

lax_coodinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokio', 2003, 32450, 0.66, 8014)
travelers_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

for passaport in sorted(travelers_ids):
    print('%s/%s' % passaport)

for country, _ in travelers_ids:
    print(country)

# another way to unpacking

coord_test = (33.9425, -118.408056)

lat, lon = coord_test

print('latitude', lat)
print('longitude', lon)

# another another way to unpacking

t = (20, 8)

print(divmod(*t))
