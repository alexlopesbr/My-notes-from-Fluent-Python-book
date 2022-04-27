# 03.09 | 109 | MappingProxiType creates a read-only mappingproxy instance from a dict

from types import MappingProxyType
d = {1: 'A'}
d_proxy = MappingProxyType(d)

print(d_proxy)
print(d_proxy[1])
# print(d_proxy[2]) => KeyError: 2


d[2] = 'B'
print(d_proxy)
