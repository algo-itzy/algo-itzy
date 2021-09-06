# git commit -m "code: Solve boj 09019 DSLR (seungjoo)"
import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    visited[start] = True
    q = deque()
    q.append([start,''])
    while q:
        cur_register, commands = q.popleft()
        if cur_register==target:
            return commands
        for command in 'DSLR':
            if command=='D':
                next_register = (cur_register*2)%10000
            elif command=='S':
                next_register = (cur_register-1)%10000
            elif command=='L':
                next_register = (cur_register%1000)*10 + cur_register//1000
            else:
                next_register = cur_register//10 + (cur_register%10)*1000
            if not visited[next_register]:
                visited[next_register] = True
                q.append([next_register,commands+command])



for _ in range(int(input())):
    start, target = map(int, input().split())
    visited = {i: False for i in range(10000)}
    print(bfs(start))