def solution(absolutes, signs):
    s = ''.join([str(signs[i])+str(absolutes[i]) for i in range(len(signs))])
    return eval(s.replace("True","+").replace("False","-"))