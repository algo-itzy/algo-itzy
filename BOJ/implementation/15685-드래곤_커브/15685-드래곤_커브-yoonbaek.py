from sys import stdin

rd = stdin.readline

up, down, left, right = (0, -1), (0, 1), (-1, 0), (1, 0)

dirs = {
    0: right, 1: up, 2: left, 3: down,
}

if __name__ == "__main__":
    N = int(rd())
    mat = [[0 for _ in range(101)] for _ in range(101)]

    for _ in range(N):
        x, y, d, g = map(int, rd().split())
        cmds = [d]

        mat[y][x] = 1

        for _ in range(g):
            stack = [c for c in cmds]
            while stack:
                cmd = stack.pop()
                cmds.append((cmd+1)%4)

        for cmd in cmds:
            c, r = dirs[cmd]
            x += c; y += r
            mat[y][x] = 1
        
    squares = 0
    for row in range(100):
        for col in range(100):
            if mat[row][col] and mat[row][col+1] and mat[row+1][col] and mat[row+1][col+1]:
                squares += 1

    print(squares)

# git commit -m "code: Solve boj 15685 드래곤 커브 (yoonbaek)"