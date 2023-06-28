def solution(s):
    return ''.join(sorted([i for i in s if ord(i)>=ord('a')], reverse=True)+sorted([i for i in s if ord(i)<ord('a')], reverse=True))