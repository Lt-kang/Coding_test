t = [chr(i) for i in range(97,123)]

a = input()


for i in range(len(t)):
    print(a.find(t[i]), end = ' ')


