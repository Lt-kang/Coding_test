def prime(n):
    list_ = []
    for i in range(1, n+1):
        if n%i==0: list_.append(i)

    return list_


while True:
    n = int(input())
    if n==-1: break
    
    n_list = prime(n)
    
    if n*2 == sum(n_list):
        n_list_str = [str(i) for i in n_list]
        print(f"{n} = ", end='')
        print(' + '.join(n_list_str[:-1]))
    else:
        print(f"{n} is NOT perfect.")
    