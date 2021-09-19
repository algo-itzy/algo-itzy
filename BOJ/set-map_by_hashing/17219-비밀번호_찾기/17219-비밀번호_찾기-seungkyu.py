# git commit -m "code: Solve boj 17219 비밀번호 찾기 (seungkyu)"
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

sites = {}
for _ in range(N):
    site, pwd = input().split()
    sites[site] = pwd

for _ in range(M):
    site = input().strip()
    print(sites[site])
