# 04.16 | 157 | Function to remove mixed tags from latin characters

import string
import unicodedata


def shave_marks_latin(txt):
    """Removes all diacritical marks from Latin base characters."""
    norm_text = unicodedata.normalize('NFD', txt)
    latin_base = False
    keepers = []

    for c in norm_text:
        if unicodedata.combining(c) and latin_base:
            continue  # skip diacritics on latin base characters

        keepers.append(c)

        # if c is a latin base character, set latin_base to True
        if not unicodedata.combining(c):
            latin_base = c in string.ascii_letters

    shaved = ''.join(keepers)

    return unicodedata.normalize('NFC', shaved)


print(shave_marks_latin('café , avião, vovô, à, açaí'))
print(shave_marks_latin('Αργυροκομείο'))
print(shave_marks_latin('Аргентина'))
