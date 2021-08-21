import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):

    N, M = map(int, input().split())
    # 회전 기능 있는 deque를 사용해서 쉽게 풀었습니다..
    numbers = deque(map(int, input().split()))
    numbers.rotate(-M)  # 음수이면 왼쪽으로 회전(왼쪽으로 숫자 밀기)

    print(f'#{test_case} {numbers[0]}')
