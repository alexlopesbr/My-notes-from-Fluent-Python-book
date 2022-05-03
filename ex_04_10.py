# 04.10 | 145 | Closer inspection of example 4.9 running on windows shows how to fix it

import os
print('========== fp ==========')
fp = open('cafe.txt', 'w', encoding='utf-8')
print(fp)
print(fp.write('café'))
fp.close()

print(os.stat('cafe.txt').st_size)

print('\n ========== fp2 =========')
fp2 = open('cafe.txt')
print(fp2)
print(fp2.encoding)
print(fp2.read())

print('\n ========== fp3 =========')
fp3 = open('cafe.txt', encoding='utf-8')
print(fp3)
print(fp3.read())

print('\n ========== fp4 =========')
fp4 = open('cafe.txt', 'rb')
print(fp4)
print(fp4.read())
