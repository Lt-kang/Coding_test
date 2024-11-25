import sys
input = sys.stdin.readline


word = input().strip() # 8진수
octal_number = int(word, 8) # 10진수로 변환
binary_number = format(octal_number, 'b') # 2진수로 변환
print(binary_number)
