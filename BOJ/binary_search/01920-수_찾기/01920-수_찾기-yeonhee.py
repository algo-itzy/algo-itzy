import sys

input = sys.stdin.readline

N = int(input())
sorted_list = sorted(list(map(int, input().split())))
M = int(input())
numbers = list(map(int, input().split()))

def binary_search(element):
    start_idx = 0
    end_idx = len(sorted_list) - 1

    while start_idx <= end_idx:
        mid_point = (start_idx + end_idx) // 2
        if sorted_list[mid_point] == element:
            return 1
        elif sorted_list[mid_point] > element:
            end_idx = mid_point - 1
        else:
            start_idx = mid_point + 1

    return 0

for number in numbers:
    print(binary_search(number))


"""
이분 탐색 : 탐색 범위를 반씩 제외시키며 찾는 알고리즘으로, 정렬된 리스트를 전제로 한다.
제가 맡은 부분이라 제 취향을 내려놓고 정석으로 풀이해봤습니다.
"""

# 꼼수 풀이

# N = input()
# A = set(input().split())
# M = input()
# numbers = input().split()

# for number in numbers:
#     print(1 if number in A else 0)
