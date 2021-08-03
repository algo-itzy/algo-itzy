import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input())
n_arr = list(map(int,input().split()))
# O(1)로 접근하기 위한 hash table입니다.
dicts = defaultdict(int)
# n회순회하며 카운팅했습니다.
for num in n_arr:
    dicts[num] +=1
M = int(input())
m_arr = list(map(int,input().split()))
# 카운팅한거 해쉬로 접근해 출력했습니다.
for m in m_arr:
    print(dicts[m],end=" ")
