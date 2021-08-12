from collections import deque

N = int(input()) # 컴퓨터의 수 N

connected = int(input()) # 연결돼 있는 컴퓨터 쌍의 수 

computer=[]
for i in range(N+1):
  computer.append([])

print(computer)

# for _ in range(connected):

# for i in range(connected):
#     a, b = map(int, input().split())


# def bfs(computer):
#     queue = deque()
#     queue.append(1)
#     cnt = 0

#     while queue: 
#         c = queue.popleft()

#         for com in computer[c]:
#             if virus[com] ==0:




