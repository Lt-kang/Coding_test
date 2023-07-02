def solution(myStr):
    myStr = myStr.replace("a",".").replace("b",".").replace("c",".").split(".")
    myStr = [w for w in myStr if w]
    return myStr if myStr else ["EMPTY"]