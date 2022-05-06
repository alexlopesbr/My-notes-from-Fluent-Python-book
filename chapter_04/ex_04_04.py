# 04.04 | 135 | Using memoryview and struct to inspect the header of a GIF image

import struct

fmt = '<3s3sHH'
with open('filter.gif', 'rb') as fp:
    img = memoryview(fp.read())

header = img[:10]

print(bytes(header))
print(struct.unpack(fmt, header))

del header
del img
