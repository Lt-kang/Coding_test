def solution(myString, pat):
    p_l = len(pat)
    m_l = len(myString)
    return sum([1 for i in range(m_l-p_l+1) if pat in myString[i:i+p_l]])