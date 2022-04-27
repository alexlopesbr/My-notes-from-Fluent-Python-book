# 03.10 && 03.11 && 03.12 | 110 | Occurrence account
# of needles occurrence in haystack, both `set` type

# 03.10
# work only with set type or frozenset type
needles = {'a', 'b', 'c'}
haystack = {'a', 'b', 'c', 'd', 'e'}

found = len(needles & haystack)

print(found)


# 03.11
# work with any iterable object
found_2 = 0
for n in needles:
    if n in haystack:
        found_2 += 1

print(found_2)

# 03.12
# another ways to do it

found_3 = len(set(needles) & set(haystack))
print(found_3)

found_4 = len(set(needles).intersection(haystack))
print(found_4)
