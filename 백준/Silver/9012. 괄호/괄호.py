n = int(input())


for _ in range(n):
    w = input()
    while True:
        if w != "" and w.replace("()","")==w: print("NO"); break
        elif w=="": print("YES"); break
        else: w = w.replace("()", "")
