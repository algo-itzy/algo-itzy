n = int(input())
x = list(map(int, input().split()))
x1 = sorted(list(set(x)))
r = {x1[i]: i for i in range(len(x1))}
print(*[r[i] for i in x])
