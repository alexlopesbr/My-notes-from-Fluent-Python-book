# 04.09 | 145 | A platform-related decoding problem (if you test this code on your computer, you may
# or may not see the problem)

print(open('cafe.txt', 'w', encoding='utf-8').write('café'))
print(open('cafe.txt').read())
