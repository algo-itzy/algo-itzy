"""
블로그에서 참고한 풀이입니다 

이진 탐색: 배열 중간에 있는 데이터의 값을 선택하고 찾고자하는 값과 비교해서 그 값보다 작으면
중간 값을 기준으로 좌측 데이터를 대상으로 탐색~ 해당 값을 찾을 때까지 반복
"""

import sys

def binary_search(a,x):
    start = 0 
    end = len(a) -1

    while start <= end:
        mid = (start + end)//2
        if x == a[mid]:
            return 1
        elif x > a[mid]:
            start = mid +1
        else: 
            end = mid -1
    return 0

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
a.sort()

m = int(input())
x = list(map(int, sys.stdin.readline().split()))

for k in range(m):
    print(binary_search(a, x[k]))


"""
시간 초과가 뜸

N = input()
list_N = list(map(int, input().split())) # N개의 정수 = A[0], A[1],,, A[N]

M = input()
list_M = list(map(int, input().split()))

for i in range (len(list_M)):
    if list_M[i] in list_N: # 리스트 M 의 각각의 인덱스를 돌았을 때, 그 원소가 리스트 N에 있는 경우 1을 출력
        print(1)
    else:
        print(0)
"""

