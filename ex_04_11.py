# 04.11 | 146 | Exploring defaults for codification

import locale, sys


expression = """
    locale.getpreferredencoding()
    type(my_file)
    my_file.encoding
    sys.stdout.isatty()
    sys.stdout.encoding
    sys.stdout.isatty()
    sys.stdout.encoding
    sys.stderr.isatty()
    sys.stderr.encoding
    sys.getdefaultencoding()
    sys.getfilesystemencoding()
"""

my_file = open('dummy', 'w')

for expression in expression.split():
    value = eval(expression)
    print(expression.rjust(30), '->', repr(value))
