# 03.05 | 101 | index_default.py: using an instance of defaultdict instead of setdefault

import collections
import re
import sys

WORD_RE = re.compile(r'\w+')

index = collections.defaultdict(list)
with open(sys.argv[0], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index[word].append(location)

# shows in alphabetical order
for word in sorted(index, key=str.upper):
    print(word, index[word])
