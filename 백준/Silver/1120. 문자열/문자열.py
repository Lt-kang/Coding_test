import sys

A, B = input().split()
# A, B = "adaabc aababbc".split()


cnt = 0
if len(A) == len(B):
    for i in range(len(A)):
        if A[i] != B[i]:
            cnt += 1

    print(cnt)
    

else:
    cnt = sys.maxsize

    for i in range(abs(len(A) - len(B))+1):
        temp_B = B[i:len(A)+i]

        temp_cnt = 0
        for j in range(len(A)):
            if A[j] != temp_B[j]:
                temp_cnt += 1

        cnt = min(cnt, temp_cnt)

    print(cnt)

