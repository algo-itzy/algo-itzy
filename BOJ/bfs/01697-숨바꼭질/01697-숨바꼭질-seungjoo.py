import sys
input = sys.stdin.readline
from collections import deque

def BFS(N,K):
    queue=deque()
    queue.append(N)
    while queue:
        cur_node = queue.popleft()
        if cur_node==K:
            return
        # 늘 작은 값부터 조사해야함. 큰값부터 하면 최솟값 비교연산까지 들어가야함.
        for next_node in (cur_node-1,cur_node+1,cur_node*2):
            if 0<=next_node<=100000 and not time[next_node]:
                time[next_node] = time[cur_node] + 1
                queue.append(next_node)

N,K = map(int,input().split())
time = [0]*100001
if K>N:
    BFS(N,K)
    print(time[K])
else:
    print(N-K)
