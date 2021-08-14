import sys
sys.stdin = open('input.txt')


def solution(n):
    if n == 1:
        return 1
    # 결과가 [1, 3, 5, 11, 21, 43, 85, ...]
    return 2*solution(n-1) - 1 if n%2 else 2*solution(n-1) + 1


for t in range(1, int(input())+1):
    n = int(input())
    print(f'#{t} {solution(n//10)}')
