from collections import deque

def bfs():
    queue = deque()
    queue.append(N)             # 수빈이 위치 N 을 큐에 넣기
    while queue:                # queue 에 값이 들어있는 동안 
        v = queue.popleft()
        if v == K:              # 동생한테 잡히면
            print(time[v])
            return 
        for next in (v-1, v+1, v*2):
            if 0<= next < maximum and not time[next]:
                time[next] = time[v] +1
                queue.append(next)

maximum = 100001                 # 0 ~ 100,000
N, K = map(int, input().split()) # 수빈이 위치 N, 동생의 위치 K
time = [0]* maximum 
bfs() 