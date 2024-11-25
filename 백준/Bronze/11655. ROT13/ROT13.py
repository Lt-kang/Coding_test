import sys
input = sys.stdin.readline


Large_alphabet = [chr(i) for i in range(65, 91)]
Small_alphabet = [chr(i) for i in range(97, 123)]

def func(s:str) -> str:
    if s in Large_alphabet:
        temp_list = Large_alphabet
    elif s in Small_alphabet:
        temp_list = Small_alphabet
    else:
        return s

    idx = temp_list.index(s)
    return temp_list[(idx + 13) - 26]

sentence = list(map(func, input()))
print(''.join(sentence))


