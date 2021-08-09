import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pokemon_num = {i: input().strip() for i in range(1, n+1)}
pokemon_name = {v: k for k, v in pokemon_num.items()}

for _ in range(m):
    p = input().strip()
    print(pokemon_num[int(p)] if p.isdigit() else pokemon_name[p])