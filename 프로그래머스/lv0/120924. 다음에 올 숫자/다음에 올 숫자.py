def check_pattern(num_list):
    if num_list[2]-num_list[1] == num_list[1]-num_list[0]: return True
    return False

def solution(common):
    if check_pattern(common): 
        d = common[1]-common[0]
        return common[-1]+d
    else:
        r = common[1]//common[0]
        return common[-1]*r