while True:
    try:
        n = int(input())
    except:
        break

    
    k = 1
    spe_num = ""
    while True:
        spe_num += str(k*n)
        _list = list(set(spe_num))
        if sorted(_list) == list(map(str, range(0, 10))):
            print(k)
            break

        k += 1
        