# 04.01 | 130 | Coding and decoding

s = 'café'
print(len(s))

b = s.encode('utf-8')
print(b)
print(len(b))

print(b.decode('utf-8'))
