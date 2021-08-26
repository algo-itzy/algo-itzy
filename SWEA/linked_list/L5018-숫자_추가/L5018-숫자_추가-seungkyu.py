import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):

    N, M, L = map(int, input().split())
    numbers = list(map(int, input().split()))

    for _ in range(M):
        idx, num = map(int, input().split())
        numbers.insert(idx, num)

    print(f'#{test_case} {numbers[L]}')
