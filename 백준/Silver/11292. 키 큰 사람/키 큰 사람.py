import sys
input = sys.stdin.readline



while True:
    n = int(input())
    if n==0: break
    else:
        l = []
        cm_list = []
        for _ in range(n):
            name, cm = list(input().split())
            l.append([name, float(cm)])
            cm_list.append(float(cm))
        mx_cm = max(cm_list)
        
        for w in l:
            if w[1]==mx_cm: print(w[0],end=' ')
        print()