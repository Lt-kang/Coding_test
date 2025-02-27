import re
import sys

input = sys.stdin.readline


sentances = []
while True:
    sentance = input()
    sentances.append(sentance)

    if 'E-N-D' in sentance:
        break


results = re.sub(r'[^a-zA-Z-]', ' ', ' '.join(sentances)).split()

_max_size = 0
_max_word = ""
for sentance in results:
    _size = len(sentance)

    if _size > _max_size:
        _max_size = _size
        _max_word = sentance


print(_max_word.lower())


