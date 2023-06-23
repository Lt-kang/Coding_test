def solution(num_list):
    answer = ["P" if i>0 else "N" for i in num_list]
    return answer.index("N") if "N" in answer else -1