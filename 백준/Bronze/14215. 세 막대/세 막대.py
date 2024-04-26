list_ = list(map(int, input().split()))

max_size = max(list_)
another_size = sum(list_) - max_size

while True:
    if max_size >= another_size:
        max_size -= 1
    else:
        print(another_size + max_size)
        break
