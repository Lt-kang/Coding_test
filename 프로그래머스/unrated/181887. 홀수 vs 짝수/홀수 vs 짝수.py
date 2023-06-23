def solution(num_list):
    odd = sum([num_list[i] for i in range(len(num_list)) if (i+1)%2!=0])
    even = sum([num_list[i] for i in range(len(num_list)) if (i+1)%2==0])
    return odd if odd>even else even