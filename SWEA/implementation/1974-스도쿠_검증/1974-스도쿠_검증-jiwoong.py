"""
# 스도쿠 검증
입력으로 9 X 9 크기의 스도쿠 퍼즐의 숫자들이 주어졌을 때,
겹치는 숫자가 없을 경우, 1을 정답으로 출력하고 그렇지 않을 경우 0 을 출력

첫 줄에 총 테스트 케이스의 개수 T
다음 줄부터 각 테스트 케이스
테스트 케이스는 9 x 9 크기의 퍼즐의 데이터

테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력
"""


def sudoku_check():
    # 스도쿠 판 2중 리스트로 생성
    sudoku_lst = []
    for number in range(9):
        sudoku_num = list(map(int, input().split()))
        sudoku_lst.append(sudoku_num)
    # 가로줄, 세로줄 겹치는 숫자 확인
    for y in range(9):
        column = []
        row = []
        for x in range(9):
            column.append(sudoku_lst[y][x])
            row.append(sudoku_lst[x][y])
        if len(set(column)) != 9 or len(set(row)) != 9:
            return 0
    # 3*3 칸 9개의 겹치는 숫자 확인
    for i in range(0, 9, 3):
        column = []
        row = []
        for b in range(i, i + 3):
            for c in range(3):
                column.append(sudoku_lst[b][c])
                row.append(sudoku_lst[c][b])
        if len(set(column)) != 9 or len(set(row)) != 9:
            return 0

    return 1


T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc} {sudoku_check()}')
