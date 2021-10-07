# git commit -m "code: Solve boj 17135 캐슬 디펜스 (jiwoong)"
import sys
from itertools import combinations

input = sys.stdin.readline

N, M, D = map(int, input().split())  # N : 행, M : 열, D : 공격 거리 제한      *궁수는 M+1행에 배치
monster = {}  # 몬스터 배치
ans = []  # 결과값
area = [t for t in range(M)]  # 0부터 M-1까지

for i in range(N):
    monster[i] = list(map(int, input().split()))
archer = list(combinations(area, 3))  # 궁수 3명 뽑아내는 조합


def game(ar, ac):
    kill = 0
    for i in range(D):  # 제한 거리만큼 반복
        check = kr = kc = 0
        for j in range(-i, i + 1):  # 왼쪽부터 차례로 탐색
            mr, mc = ar - i - 1 + abs(j), ac + j
            if mr < 0 or mc < 0 or mc > M - 1:
                continue
            if monster[mr][mc] == 1:
                check, kr, kc = 1, mr, mc
                break
        if check:
            kill = (kr, kc)
            break
    return kill


def result(archers):
    cnt = 0
    x_kill = {}
    for i in range(N):  # 궁수의 input 위치
        killed = {}
        for archer in archers:
            tmp = game(N - i, archer)  # 각 위치의 궁수들이 kill한 몬스터의 input,ac 반환
            if tmp:
                killed[tmp] = 0
                x_kill[tmp] = 0
        cnt += len(killed)
        for ac in killed:
            monster[ac[0]][ac[1]] = 0
    for ac in x_kill:
        monster[ac[0]][ac[1]] = 1
    return cnt


for i in archer:  # 궁수의 위치에 따라 반복
    ans.append(result(i))
print(max(ans))
