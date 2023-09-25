from collections import Counter
import sys
#input = sys.stdin.readline

def palindrome(word):
    answer = ""
    word = list(word)
    word_set = list(set(word))

    if len(word)%2==0:
        word_set.sort()
        word_count = [word.count(w) for w in word_set]

        for w in range(len(word_set)):
            answer += word_set[w]*(word_count[w]//2)
        answer = answer + answer[::-1]

        return str(''.join(answer))
    else:
        word_set.sort(key= lambda x:(x, word.count(x)))
        word_count = [word.count(w) for w in word_set]
        word_odd = [w  for w in word_set if word.count(w)%2!=0]
        for w in range(len(word_set)):
            answer += word_set[w]*(word_count[w]//2)
        answer = answer + word_odd[0] + answer[::-1]
        
        return str(''.join(answer))



n = input()
counter_n = Counter(n)
check_odd = [1 if i%2!=0 else 0 for i in counter_n.values()]
if (len(n)%2==0 and sum(check_odd)==0) or\
    (len(n)%2!=0 and sum(check_odd)==1):
    print(palindrome(n))

else:
    print("I'm Sorry Hansoo")
