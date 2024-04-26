while True:
    list_ = list(map(int, input().split()))
    if list_ == [0, 0, 0]: break

    if sum(list_)-max(list_) <= max(list_): 
        print("Invalid")

    elif len(set(list_))==3: print("Scalene")
    elif len(set(list_))==2: print("Isosceles")
    else: print("Equilateral")