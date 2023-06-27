def trans_one(num):
    cnt = 0
    if num==1: return 0
    while True:
        cnt += 1
        if num%2==0: num //= 2
        elif num%2!=0: num = (num-1)//2
        
        if num==1: 
            return cnt
        
def solution(num_list):
    return sum([trans_one(i) for i in num_list])


# 개선코드
def solution(num_list):
    return sum(len(bin(i)) - 3 for i in num_list)

# bin() - 정수를 이진수 문자열로 변환하는 함수
# 예를 들어 i=12 일때, bin(i) 를 하면 '0b1100' 이 됩니다. 
# 여기서 우리는 마지막으로 남겨야 하는 1; 
# 즉 2^0인 맨끝의 '0'과 과 이진수를 나타내는 앞의 '0b' 총 길이 3을 제외한 나머지 숫자들인 "110" 을 없애는 것이 목표값이 되는데, 
# 이는 각 자리마다 2를 나누는 횟수기 때문에 "110"의 길이인 3이 됩니다. 홀 수 일 때는 어차피 -1을 해서 짝수로 만들기 때문에 가능합니다.
