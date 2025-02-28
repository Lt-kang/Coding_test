line = []
while True:
    try:
        _temp = input()
    except:
        break
    
    line.append(_temp)


print(sum(list(map(int, ''.join(line).split(",")))))
