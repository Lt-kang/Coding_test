

num = input()
t = 0

for i in range(1,int(num)+1):
    i = str(i)
    if 100>int(i):
        t +=1
    elif int(i)>100:
        if int(i[0])-int(i[1]) == int(i[1])-int(i[2]):
            t +=1

print(t)
