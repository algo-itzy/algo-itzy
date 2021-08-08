"""
첫 줄에는 테이스 케이스 개수 T
그 다음 줄에는 M(가로길이: 1<=M<=50), 세로길이(1<=N<50), 배추 심어져있는 위치 개수(1<=X<=2500)
나머지는 배추의 위치가 주어짐  
"""

from collections import deque 

T = int(input())

def bfs(x,y):                           # bfs 함수 구현
    dx =[0,0, -1,1]                     # 상하좌우 좌표 생성
    dy =[1,-1, 0,0]
    queue = deque()
    queue.append((x,y))                 # 좌표 값을 덱에 넣어줌

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx>=0 and nx<N and ny>=0 and ny<M:
                if field[nx][ny] == 1:
                    queue.append((nx,ny))
                    field[nx][ny] =2

for i in range(T):
    M, N, K = map(int, input().split())
    field = [[0]*M for _ in range(N)]   # 초기화가 되어있는 배추밭 생성하기 
    
                                        # ex) M=5, N=3
                                        # [0,0,0,0,0]
                                        # [0,0,0,0,0]
                                        # [0,0,0,0,0]
    for i in range(K):                  # 배추가 심어져있는 개수만큼 for 문 돌아 해당 원소에 1 넣어주기
        a,b = map(int, input().split())
        field[b][a] = 1                 

    cnt=0

    for i in range(N):
        for j in range(M):
            if field[i][j]==1:
                bfs(i,j)
                cnt+=1
    print(cnt)

 """"
 주의해야할 포인트:
 a b 는 각각 가로, 세로의 위치지만 -> 5,3

 위의 2차원 배열에서 맨 오른쪽 아래에 있는 값을 확인하고 싶은 경우
 세로 가로로 접근해야 됨 -> 3, 5
 """   