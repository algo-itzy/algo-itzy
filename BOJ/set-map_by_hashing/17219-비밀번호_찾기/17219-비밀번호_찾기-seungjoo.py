# git commit -m "code: Solve boj 17219 비밀번호 찾기 (seungjoo)"
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = {}
for _ in range(N):
    address, pw = input().split()
    dic[address] = pw
for _ in range(M):
    print(dic[input().rstrip()])