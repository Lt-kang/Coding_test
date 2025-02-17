op_map = {'+': lambda x, y: x+y,
          '-': lambda x, y: x-y,
          '*': lambda x, y: x*y,
          '/': lambda x, y: x//y,
          }


n = int(input())
for _ in range(n):
    q = input()
    a, op, b, _, answer = q.split()
    print('correct' if op_map[op](int(a), int(b)) == int(answer) else 'wrong answer')



            