
n = list(input())

answer = ""
temp = ""
temp_ = ""
switch = False

for w in n:
    if "<"==w: 
        answer += ''.join(temp[::-1])
        temp = ""
        temp_ = ""
        switch = True

    if " " == w and not switch:
        answer += ''.join(temp[::-1])
        answer += " "
        temp = ""
    elif ">"==w:
        temp_ += w
        answer += temp_
        switch = False
    elif not switch:
        temp += w
    elif switch:
        temp_ += w

answer += ''.join(temp[::-1])
print(answer)