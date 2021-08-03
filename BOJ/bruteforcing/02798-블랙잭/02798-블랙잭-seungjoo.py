
import sys
input = sys.stdin.readline

# 2차 브루트포스 탐색 통과.(모든 조합의 수 검증.)
N,M = map(int,input().split())
cards = list(map(int,input().split()))
max_num=0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            total = cards[i]+cards[j]+cards[k]
            if total <=M:
                if max_num < cards[i]+cards[j]+cards[k]:
                    max_num = cards[i]+cards[j]+cards[k]

print(max_num)


# 1차 DFS 탐색 시간초과
# def DFS(start,depth,sum_n):
#     global max_sum
#     if depth==3 and sum_n <= M:
#         max_sum = max(max_sum,sum_n)
#         return
#     for i in range(start,N):
#         if not visited[i]:
#             visited[i]=True
#             DFS(i+1,depth+1,sum_n+cards[i])
#             visited[i]=False

# N,M = map(int,input().split())
# cards = list(map(int,input().split()))
# visited = [False]*(N+1)
# max_sum=0
# DFS(0,0,0)
# print(max_sum)