# 04.19 | 159 | Using locale.strzfrm function as sort key

import locale

print(locale.setlocale(locale.LC_COLLATE, 'pt_BR.UTF-8'))

fruits = ['cajú', 'atemoia', 'cajá', 'açaí', 'acerola']
sorted_fruits = sorted(fruits, key=locale.strxfrm)

print(sorted_fruits)
