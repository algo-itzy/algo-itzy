import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    n = int(input())
    prices = list(map(int, input().split()))

    result = 0
    highest = 0

    for i in range(n-1, -1, -1):
        if prices[i] < highest:
            result += highest - prices[i]
        else:
            highest = prices[i]

    print(f'#{t} {result}')

"""
풀기 전에 swea 댓글을 봐버렸어요.........
"""
