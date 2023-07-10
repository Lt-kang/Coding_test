def solution(p):
    x = [i for i in p.split(" + ") if "x" in i]
    c = [int(i) for i in p.split(" + ") if "x" not in i]
    x = [int(w.replace("x","")) if w!="x" else 1 for w in x]
    
    answer_x = "x" if sum(x)==1 else f'{sum(x)}x' if sum(x)!=0 else ""
    answer_c = str(sum(c)) if sum(c)!=0 else ""
    return  answer_x +" + "+ answer_c if sum(x) and sum(c) != 0 else answer_x + answer_c

    