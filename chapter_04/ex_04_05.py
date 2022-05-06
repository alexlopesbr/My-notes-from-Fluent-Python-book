# 04.05 | 136 | The string "El Niño" encoded with three codecs generating
# very different sequences of bytes

for codec in ['utf-8', 'utf-16', 'utf-32']:
    print(codec, 'El Niño'.encode(codec), sep='\t')
