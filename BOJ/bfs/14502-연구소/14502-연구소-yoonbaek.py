from sys import stdin
from collections import deque

rd = lambda : map(int, stdin.readline().split())
moves = ((-1, 0), (1, 0), (0, -1), (0, 1))

# BFS
def spread(starts, lab):
    q = deque(starts)
    spread_cnt = 0
    while q:
        now = q.pop()

        for x, y in moves:
            x += now[0]
            y += now[1]

            if 0 <= x < M and 0 <= y < N:
                if not lab[y][x]:
                    spread_cnt += 1
                    lab[y][x] = 1
                    q.append((x,y))
    
    return spread_cnt

if __name__ == "__main__":
    N, M = rd()
    lab = [list(rd()) for _ in range(N)]

    starts, empties = [], []
    for row in range(N):
        for col in range(M):
            if not lab[row][col]:
               empties.append((col, row))
            if lab[row][col] == 2:
                starts.append((col, row))
    len_empties = len(empties)

    safe_cnt = 0
    for i in range(len_empties):
        for j in range(i):
            for k in range(j):
                wall1, wall2, wall3 = empties[i], empties[j], empties[k]

                lab[wall1[1]][wall1[0]] = 1
                lab[wall2[1]][wall2[0]] = 1
                lab[wall3[1]][wall3[0]] = 1

                spread_cnt = spread(starts, lab)

                for empty in empties:
                    lab[empty[1]][empty[0]] = 0

                safe_cnt = max(safe_cnt, len_empties - spread_cnt -3)

    print(safe_cnt)

# git commit -m "code: Solve boj 14502 연구소 (yoonbaek)"