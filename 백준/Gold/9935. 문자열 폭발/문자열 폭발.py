word = input()
c4_word = input()

last_word = c4_word[-1]
c4_word_1 = c4_word[:-1]
word_size = len(c4_word)

stack = []
for c in word:
    if c == last_word and ''.join(stack[word_size*-1:]).endswith(c4_word_1):
        for _ in range(word_size-1):
            stack.pop()
    else:
        stack.append(c)
    

print("FRULA" if not stack else ''.join(stack))