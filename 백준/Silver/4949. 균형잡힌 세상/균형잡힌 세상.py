import re

def check_word(word):
    if word == ".": return -1

    new_word = re.sub(r'[^\[\]()\.]', "" , word)
    while True:
        old_word = new_word[:]
        new_word = new_word.replace("[]","").replace("()","")
        if old_word == new_word:
            return new_word
        
        

while True:
    t = input()
    if t==".": break
    else: 
        if check_word(t) == -1: break
        elif check_word(t) == ".": print("yes")
        else: print("no")
