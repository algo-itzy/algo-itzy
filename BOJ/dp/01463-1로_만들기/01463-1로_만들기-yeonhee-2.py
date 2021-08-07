# top-down 방식 dp
# dp 연습용 코드입니다. 백준 제출 시 메모리가 초과됩니다.

import sys
sys.setrecursionlimit(10**6)

def get_one(N):
    # base case
    if N == 1:
        return 0

    # recursive case
    # 재귀 호출을 이용하는 것 외에는 bottom-up과 동일
    result = get_one(N-1) + 1

    if N % 3 == 0:
        result = min(get_one(N//3)+1, result)
    if N % 2 == 0:
        result = min(get_one(N//2)+1, result)

    return result

print(get_one(int(input())))