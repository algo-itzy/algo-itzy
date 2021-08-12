"""
# 최소 힙
배열에 자연수 x를 넣는다.
배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.

첫째 줄에 연산의 개수 n(1 ≤ n ≤ 100,000)
다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x
만약 x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산이고,
x가 0이라면 배열에서 가장 작은 값을 출력하고 그 값을 배열에서 제거

0이 주어진 회수만큼 답을 출력
배열이 비어 있는 경우인데 가장 작은 값을 출력하라고 한 경우에는 0을 출력
"""

import sys
import heapq

input = sys.stdin.readline
n = int(input())
ans = []

for _ in range(n):
    x = int(input())
    if x == 0:
        if len(ans) == 0:
            print(0)
        else:
            print(heapq.heappop(ans))
    else:
        heapq.heappush(ans, x)
