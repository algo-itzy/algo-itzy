D = ((), (1,0), (-1,0), (0,-1), (0,1))  # 동서북남


def move(n, a):
    if n == 1:
        return [0, a[3], a[2], a[6], a[1], a[5], a[4]]
    elif n == 2:
        return [0, a[4], a[2], a[1], a[6], a[5], a[3]]
    elif n == 3:
        return [0, a[2], a[6], a[3], a[4], a[1], a[5]]
    elif n == 4:
        return [0, a[5], a[1], a[3], a[4], a[6], a[2]]


n, m, y, x, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cmds = list(map(int, input().split()))
dice = [0] * 7

for cmd in cmds:
    nx, ny = x + D[cmd][0], y + D[cmd][1]

    if 0 <= nx < m and 0 <= ny < n:
        x, y = nx, ny

        dice = move(cmd, dice)

        if not arr[y][x]:
            arr[y][x] = dice[-1]
        else:
            dice[-1] = arr[y][x]
            arr[y][x] = 0

        print(dice[1])