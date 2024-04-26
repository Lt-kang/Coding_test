def solution(word):
    size = len(word)
    for i in range(1 + int(size**1/2)):
        if word[i] != word[-1 -i]:
            return 0
        
    return 1

print(solution(input()))