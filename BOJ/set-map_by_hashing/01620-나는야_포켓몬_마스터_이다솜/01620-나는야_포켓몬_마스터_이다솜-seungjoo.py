import sys
input = sys.stdin.readline
from collections import defaultdict

# 검색은 hash table
N,M = map(int,input().split())
poc_num = defaultdict(int)
poc_name = defaultdict(str)

for i in range(1,N+1):
    a = input().rstrip()
    poc_num[a] = i
    poc_name[i] = a

for _ in range(M):
    b = input().rstrip()
    if b.isdigit():
        print(poc_name[int(b)])
    else:
        print(poc_num[b])