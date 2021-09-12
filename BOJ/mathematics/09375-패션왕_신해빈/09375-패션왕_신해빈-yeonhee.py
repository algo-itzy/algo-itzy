import sys
from collections import defaultdict

input = sys.stdin.readline

for _ in range(int(input())):
    clothes = defaultdict(int)

    for _ in range(int(input())):
        cloth, c_type = input().split()
        clothes[c_type] += 1

    result = 1

    for value in clothes.values():
        result *= value+1

    print(result-1)
