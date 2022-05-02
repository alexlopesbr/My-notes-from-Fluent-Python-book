# 04.06 | 138 | Byte encoding: success and error handling

city = 'São Paulo'

city.encode('utf-8')  # b'S\xc3\xa3o Paulo'
city.encode('utf_16')  # b'\xff\xfeS\x00\xe3\x00o\x00 \x00P\x00a\x00u\x00l\x00o\x00'
city.encode('iso-8859-1')  # b'S\xe3o Paulo'
city.encode('cp437', errors='ignore')  # b'So Paulo'
city.encode('cp437', errors='replace')  # b'S?o Paulo'
city.encode('cp437', errors='xmlcharrefreplace')  # b'S&#227;o Paulo'
