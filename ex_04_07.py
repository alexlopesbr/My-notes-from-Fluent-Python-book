# 04.07 | 139 | Decoding str to bytes: success and error handling

octets = b'Montr\xe9al'


print(octets.decode('cp1252'))
print(octets.decode('iso-8859-7'))
print(octets.decode('koi8-r'))
print(octets.decode('utf-8', errors='replace'))
