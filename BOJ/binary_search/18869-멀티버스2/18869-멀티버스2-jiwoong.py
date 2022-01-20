# git commit -m "code: Solve boj 18869 멀티버스2 (jiwoong)"
import sys

input = sys.stdin.readline

M, N = map(int, input().split())

planet = [list(map(int, input().split())) for _ in range(M)]

arr = [[] for _ in range(M)]
dict = {}
for i in range(M):
    multi = sorted(list(set(planet[i])))
    for j in range(len(multi)):
        dict[multi[j]] = j
    for x in (planet[i]):
        arr[i].append(dict[x])

arr.sort()
cnt, ans = 1, 0
for i in range(1, M):
    if arr[i] == arr[i - 1]:
        cnt += 1
    else:
        ans += cnt * (cnt - 1) // 2
        cnt = 1

ans += cnt * (cnt - 1) // 2
print(ans)