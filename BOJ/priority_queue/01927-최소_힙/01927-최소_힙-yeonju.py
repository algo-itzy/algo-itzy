import heapq
import sys

input = sys.stdin.readline
N = int(input())

heap = []

for _ in range(N): 
    x = int(input())                    # 배열에 자연수 x 를 넣음

    if x >0:                            # x 가 자연수이면 
        heapq.heappush(heap,x)

    else:                               # x 가 0이면
        if heap: 
            print(heapq.heappop(heap))
        else:                           # 배열이 비어있는 경우, 0을 출력
            print(0)

# heappop():
# 가장 작은 원소를 힙에서 겱괏값으로 리턴 + 동시에 제거 
# N = int(input()) # 연산의 개수 N 




# 아래 방식으로 하려고 했더니 안 됨. heap 을 이용해야하는 문제인 듯

# arr =[]
# for x in range(N):
#     if x> 0:
#         arr.append(x)
#         arr.sort()
#     else: 
#         print(arr[0])