import re
def solution(myString):
    pattern = "[a-l]"
    return re.sub(pattern, "l", myString)