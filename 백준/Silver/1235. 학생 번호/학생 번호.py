def checkSameSize(list_=list):
    listLen = len(list_)
    setLen = len(set(list_))

    return True if listLen == setLen else False
    

n = int(input())
list_ = [input() for _ in range(n)]
answer = 0
length = len(list_[0])

for i in range(1,length + 1):
    if n > 10**i: pass
    else:
        newList_ = []
        for w in list_:
            newList_.append(w[length-i:length])
        
        if not checkSameSize(newList_):
            pass
        else:
            answer = i
            break

print(answer)