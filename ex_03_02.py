# index0.py uses dict.get to fetch and update a list of word occurrences from the index
# (a better solution will be presented in example 3.4)

""""Create an index that mapping word -> list of occurrences"""

import re
import sys

WORD_RE = re.compile(r'\w+')
test = 'teste'

index = {}
with open(sys.argv[0], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            occurrences = index.get(word, [])
            occurrences.append(location)
            index[word] = occurrences

# shows in alphabetical order
for word in sorted(index, key=str.upper):
    print(word, index[word])
