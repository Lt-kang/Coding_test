word_list = [input() for _ in range(3)]

answer = 0
if word_list[0].isnumeric():
    answer = int(word_list[0]) + 3

elif word_list[1].isnumeric():
    answer = int(word_list[1]) + 2

elif word_list[2].isnumeric():
    answer = int(word_list[2]) + 1


# print("========================")
if answer%3==0 and answer%5==0:
    print("FizzBuzz")

elif answer%3==0 and answer%5!=0:
    print("Fizz")

elif answer%3!=0 and answer%5==0:
    print("Buzz")

else:
    print(answer)
