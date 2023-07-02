def solution(q, r, code):
    return ''.join([w for idx, w in enumerate(code) if idx%q==r])