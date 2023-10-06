while True:
    try:
        n = int(input())
    except:
        break


    one_ = 1
    cnt = 1
    while True:
        if one_%n==0:
            print(cnt)
            break
        else:
            one_ = 1+one_*10
            cnt += 1
