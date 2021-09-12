n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)][::-1]
res = 0

for x in arr:
    if k == 0:
        break
    
    res += k//x
    k %= x

print(res)