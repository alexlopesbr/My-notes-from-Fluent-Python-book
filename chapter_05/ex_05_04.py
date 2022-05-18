# 05.04 | 177 | Sorting a list of words according to their inverse spelling

from ex_05_03 import fruits


def reverse(word):
    return word[::-1]


# print(reverse('testing'))

print(sorted(fruits, key=reverse))
