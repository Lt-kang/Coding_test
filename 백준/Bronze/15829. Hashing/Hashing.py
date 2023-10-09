
n = int(input())
l = list(input())

answer = [(ord(l[i])-96)*31**i for i in range(n)]
print(sum(answer)%1234567891)

