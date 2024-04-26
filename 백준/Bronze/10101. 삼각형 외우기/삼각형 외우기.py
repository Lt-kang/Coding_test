list_ = [int(input()) for _ in range(3)]

if sum(list_)==180:
    if len(set(list_))==1: print("Equilateral")
    elif len(set(list_))==2: print("Isosceles")
    elif len(set(list_))==3: print("Scalene")
else:
    print("Error")