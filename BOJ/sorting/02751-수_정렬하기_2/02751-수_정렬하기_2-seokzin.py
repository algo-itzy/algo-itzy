import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]

nums.sort()

# print(*nums, sep='\n')

for num in nums:
  sys.stdout.write(str(num) + '\n')

# 파이썬 정렬 내장 메서드 -> O(nlogn)
# 1. 시간 초과 - PyPy3으로 바꾸고 성공 (메모리는 거의 3배)
# 2. 시간 단축 - readline 도입시 1732ms -> 840ms
# 3. 시간 단축 - write 도입시 840ms -> 760ms

"""
git commit -m "code: Solve boj 02751 수 정렬하기 2 (seokzin)"
"""