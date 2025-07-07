number = input()


i = 1
while True:
    for j in str(i):
        if number.startswith(j):
            number = number[1:]

    if number == "":
        print(i)
        exit()
    else:
        i += 1