# 04.20 | 161 | Using the pyuca.Collator.sort_key method

# better run in terminal:
import pyuca

coll = pyuca.Collator()

fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
sorted_fruits = sorted(fruits, key=coll.sort_key)

sorted_fruits
