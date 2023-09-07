def p_list(num):

    post_p = [0,1,1,1,2,2]
    if num < 6: return post_p[num]

    else:
        p = [0]*(num+1)
        for i in range(6):
            p[i] = post_p[i]
        n = 6
        while n<=num:
            p[n] = p[n-5]+p[n-1]
            n += 1
    return p[num]

n = int(input())

for i in range(n):
    t = int(input())
    print(p_list(t))

