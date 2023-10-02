import sys; input = sys.stdin.readline


def change_num(num):
    num = str(num)
   
    num_list = ['zero','one','two','three','four','five','six','seven','eight','nine']

    if int(num)>=10:
        return num_list[int(num[0])]+" "+num_list[int(num[1])]
    else:
        return num_list[int(num[0])]+" "

s, e = list(map(int, input().split()))

l = [str(i) for i in range(s,e+1)]
l.sort(key= lambda x: (change_num(x)))

for i in range(len(l)):
    if i!=0 and i%10==0: print()

    print(l[i],end=' ')

