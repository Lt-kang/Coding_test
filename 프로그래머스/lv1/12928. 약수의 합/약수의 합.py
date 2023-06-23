from math import sqrt
def solution(n):
    answer = []
    for i in range(1, int(sqrt(n))+1): # 정수 n의 약수는 1부터 정수 n의 제곱근 중 나눈 나머지가 0인 i와 n을 i로 나눈 값 두가지가 n의 약수가 된다.
        if n%i==0: 
            answer.append(i)
            answer.append(n//i)
    return sum(list(set(answer))) # 이를테면 정수 n이 4일 경우 약수가 [1,2,4]가 되는데 위 식을 사용하면 [1,2,2,4]가 되므로 중복수를 제거하기 위해 set() 함수를 사용하였다.

