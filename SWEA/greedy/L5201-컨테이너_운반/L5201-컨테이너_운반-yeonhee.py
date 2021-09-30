import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    freight = sorted(list(map(int, input().split())), reverse=True)
    capacity = sorted(list(map(int, input().split())), reverse=True)
    result = [0] * m

    for i in range(n):
        for j in range(m):
            if freight[i] <= capacity[j]:
                if not result[j]:
                    result[j] = freight[i]
                    break

    print(f'#{t} {sum(result)}')
