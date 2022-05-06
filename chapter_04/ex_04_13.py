# 04.13 | 154 | bormeq.py normalized Unicode string comparison
import unicodedata


def nfc_equal(s1, s2):
    return unicodedata.normalize('NFC', s1) == unicodedata.normalize('NFC', s2)


s1 = 'café'
s2 = 'cafe\u0301'

print(s1 == s2)
print(nfc_equal(s1, s2))
print(nfc_equal('A', 'a'))
