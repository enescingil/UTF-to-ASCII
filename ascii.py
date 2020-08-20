#UTF to ASCI converter
#Author: enestos

import sys

from idna import unichr

word = sys.argv[1]
split_word = list(word)

for i in split_word:
    new_value = ord(i)
    new_list = [new_value]
    print(new_list)
