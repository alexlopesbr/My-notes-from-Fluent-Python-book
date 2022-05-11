# 2.3 | 48 | the same list created by a listcomp and a map/filter composition

symbols = '$¢£¥€¤'

# List Comprehension
beyond_ascii_list_comp = [ord(s) for s in symbols if ord(s) > 127]
# print(beyond_ascii_list_comp)


# Map/Filter
beyond_ascii_map_filter = list(filter(lambda c: c > 127, map(ord, symbols)))
# print(beyond_ascii_map_filter)
