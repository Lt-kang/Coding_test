from collections import defaultdict
import sys
input = sys.stdin.readline

_recipe = defaultdict(int)

for _ in range(int(input().strip())):
    drink, proportion = input().strip().split()
    _recipe[drink] += int(proportion)


result = False
for k1, v1 in _recipe.items():
    for k2, v2 in _recipe.items():
        if k1 == k2: continue

        if int(min(v1, v2)*1.618) == int(max(v1, v2)):
            result = True
            

print("Delicious!" if result else "Not Delicious...")
