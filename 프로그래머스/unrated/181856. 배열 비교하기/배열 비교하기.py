def solution(arr1, arr2):
    if len(arr2)>len(arr1): answer = -1
    elif len(arr2)<len(arr1): answer = 1    
    elif len(arr2)==len(arr1):
        if sum(arr2)>sum(arr1): answer = -1
        elif sum(arr2)<sum(arr1): answer = 1
        else: answer = 0      
    return answer

# 개선 코드
def solution(arr1, arr2):
    arr1, arr2 = [[sum(arr1), sum(arr2)], [len(arr1), len(arr2)]][len(arr1) != len(arr2)]
    # A, B = [[A1, B1],[A2,B2]][True/False] 형태의 구문이며 가장 뒷부분이 True일 경우 [A1, B1]이 각각 A, B에 삽입되며 False일 경우 그 반대이다.
    
    return (arr1 != arr2)*(-1 if arr2 > arr1 else 1)
    # 길이(len)가 같지 않을 경우 arr1, arr2에는 각각 List 요소의 합이 선언되어 있음.
    # 길이(len)가 같을 경우 arr1, arr2에는 각각 List의 길이가 선언되어 있음.
    # arr1 == arr1가 성립될 경우 False가 되며 False의 정수값인 0이 되므로 return 값은 0
    
