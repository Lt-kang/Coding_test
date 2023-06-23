str_list = list(input())
for i in range(len(str_list)):
    if ord(str_list[i])>90: str_list[i] = chr(ord(str_list[i])-32)
    else: str_list[i] = chr(ord(str_list[i])+32)
print(''.join(str_list))
