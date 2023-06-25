def solution(absolutes, signs):
    s = ''.join([str(signs[i])+str(absolutes[i]) for i in range(len(signs))])
    return eval(s.replace("True","+").replace("False","-"))


# 개선 코드
def solution(absolutes, signs):
    return sum([2*x*y - x for x, y in zip(absolutes, signs)])

# True = 1, False = 0 임을 활용한 코드.
# False일 경우 2*x*y 부분은 0이 되고 -x만 남음으로 음수가 되고
# True일 경우 2*x*y 부분은 2*x가 되고 -x를 연산하게되면 x만 남음으로 정수가 됨.
