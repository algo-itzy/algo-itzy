from sys import stdin, stdout

rd = lambda: map(int, stdin.readline().split())
wr = stdout.write

move_dict = {
    1: (1, 0), 2: (-1, 0), 3: (0, -1), 4: (0, 1),
}


def roll(move):
    # E
    if move == 1:
        dice[0], dice[5] = dice[5], dice[0]
        dice[5], dice[1] = dice[1], dice[5]
        dice[1], dice[4] = dice[4], dice[1]
    # W
    if move == 2:
        dice[0], dice[4] = dice[4], dice[0]
        dice[4], dice[5] = dice[5], dice[4]
        dice[1], dice[4] = dice[4], dice[1]
    # N
    if move == 3:
        dice[3], dice[0] = dice[0], dice[3]
        dice[1], dice[3] = dice[3], dice[1]
        dice[2], dice[1] = dice[1], dice[2]
    # S
    if move == 4:
        dice[0], dice[2] = dice[2], dice[0]
        dice[1], dice[2] = dice[2], dice[1]
        dice[1], dice[3] = dice[3], dice[1]


if __name__ == "__main__":
    N, M, row, col, K = rd() # tq...
    dice = [0] * 6

    mat = []
    for _ in range(N):
        mat.append(list(rd()))

    # time: 84ms --> 68ms
    # for 표현에 함수 집어 넣지 않기
    moves = rd()
    for move in moves:
        x, y = move_dict[move]
        col += x
        row += y
        if 0 <= col < M and 0 <= row < N:
            roll(move)
            if mat[row][col]:
                dice[1] = mat[row][col]
                mat[row][col] = 0
            else:
                mat[row][col] = dice[1]
            wr(f"{dice[0]}\n")
        else:
            col -= x
            row -= y

# git commit -m "code: Solve boj 14499 주사위 굴리기 (yoonbaek)"