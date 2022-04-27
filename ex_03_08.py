# 03.08 | 107 | StrKeyDictm always converts non-string keys to str - on insert, update and query

import collections


class StrKeyDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        print(self.data)
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item


d = StrKeyDict([('2', 'two'), ('4', 'four')])

print(d['2'])
print(d[2])
