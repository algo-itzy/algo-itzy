import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    result = [1001]

    for _ in range(m):
        numbers = list(map(int, input().split()))

        for i in range(len(result)):
            if result[i] > numbers[0]:
                # result = result[:i] + numbers + result[i:] : 시간초과
                result[i:i] = numbers
                break

    print(f'#{t}', *result[-11:-1][::-1])
