# 첫글자 대문자 or _
# 대문자 + _
# 마지막 _
# __

def error_Check(word):
    if word[0].isupper(): return True
    if any(char.isupper() for char in word) and "_" in word: return True
    if word[-1] == "_"  or word[0]=="_": return True
    if "__" in word: return True

    return False

def java_to_cpp(word):
    answer = ""
    for c in word:
        if c.isupper():
            answer += "_"
            answer += c.lower()
        else:
            answer += c

    return answer


def cpp_to_java(word):
    answer = ""
    sw = False
    for c in word:
        if c == "_":
            sw = True
        elif sw:
            answer += c.upper()
            sw = False
        else:
            answer += c

    return answer


word = input()


if error_Check(word):
    print("Error!")
elif "_" in word:
    print(cpp_to_java(word))
elif any(char.isupper() for char in word):
    print(java_to_cpp(word))
else:
    print(word)