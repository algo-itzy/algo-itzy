def count_row(n, target, puzzle):
    sum_seat = 0
    for row in range(n):
        cnt = 0
        cells = []
        for column in range(n):
            if puzzle[row][column]:
                cnt += 1
            else:
                if cnt:
                    cells.append(cnt)
                cnt = 0
        cells.append(cnt)
        sum_seat += cells.count(target)
    return sum_seat


def find_seat(size, length):
    n = size
    l = length
    answer = 0

    puzzle = [list(map(int, input().split())) for _ in range(n)]
    answer += count_row(n, l, puzzle)

    new_puzzle = [k for k in zip(*puzzle)]
    answer += count_row(n, l, new_puzzle)

    return answer


for test in range(1, int(input())+1):
    N, K = map(int, input().split())
    print(f'#{test} {find_seat(N, K)}')
