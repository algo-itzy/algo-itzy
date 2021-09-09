# 문제 접근을 잘 못하겠어서 ㅠ-ㅠ 풀지를 못했습니다 조금 더 공부하고 올리겠습니다

# 현재 위치와 현재까지의 경로
# 입력 받은 a 를 queue 에 삽입
# a를 이용해 d,s,l,r 수행하고 가능한 결과값은 queue 에 삽입
from collections import deque
import sys
input = sys.stdin.readline()



def bfs(start, end):
    queue = deque([start, ""])

    if n == end:

    while queue:
        n, func = q.popleft()

t = int(input())
for tc in range(t):
    a, b = map(int, input().split())
    arr = [0 for i in range(10000)]
    
# git commit -m "code: Solve boj 09019 DSLR (yeonju)"