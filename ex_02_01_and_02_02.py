# 2.1 | 30 | create a list of Unicodes codes (Codepoints) from a string

symbols = '$¢£¥€¤'
codes = []

for symbol in symbols:
    codes.append(ord(symbol))


# print(codes)


# 2.2 | 30 | create a list of Unicodes codes (Codepoints) from a string


codes = [ord(symbol) for symbol in symbols]

# print(codes)

# ========================

x = 'abc'

dummy = [ord(x) for x in x]

print(dummy)
print(x)
