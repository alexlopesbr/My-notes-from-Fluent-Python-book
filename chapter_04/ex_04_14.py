# 04.14 | 156 | Function to remove all combined tags (sanitize.py module)

import unicodedata


def shave_marks(txt):
    """Remove all marks and diacritics from a string."""
    norm_txt = unicodedata.normalize('NFD', txt)
    shaved = ''.join(c for c in norm_txt if not unicodedata.combining(c))
    return unicodedata.normalize('NFC', shaved)
