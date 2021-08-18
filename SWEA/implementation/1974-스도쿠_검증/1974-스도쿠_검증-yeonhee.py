import sys
sys.stdin = open('input.txt')

# 판단 기준이 될 set
num_set = set(range(1, 10))

for t in range(1, int(input())+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    result = 1

    # 가로
    for r in range(9):
        if set(sudoku[r]) != num_set:
            result = 0

    # 세로
    for c in range(9):
        tmp = set()
        for r in range(9):
            tmp.add(sudoku[r][c])
        if tmp != num_set:
            result = 0

    # 3 X 3
    for i in (0, 3, 6):
        for j in (0, 3, 6):
            tmp = set()
            for r in range(i, i+3):
                tmp.update(sudoku[r][j:j+3])
            if tmp != num_set:
                result = 0

    print(f'#{t} {result}')
