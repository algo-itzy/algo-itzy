import sys
from math import lcm  # 최소공배수 이용


def solve(a, b):
    cnt = 1
    lcm_num = lcm(M, N)

    while a!=M or b!=N:  # 최종날짜까지 진행
        if a==x:  # x를 기준으로, x가 같으면 한 바퀴만큼 돌리면서 검사
            cnt += M
            b += M
            if b > N:
                b = b%(N)
                if b == 0:
                    b = N
        else:  # x를 기준으로 x와 다르면 일단 같게 만들어줌
            cnt += x-a
            b += x-a
            a = x
            
            if b > N:
                b = b%(N)
                if b == 0:
                    b = N

        if a==x and b==y:  # 목표 도달하면 바로 return
            return cnt

        if cnt > lcm_num:  # 검사 중 날짜수(lcm_num) 넘어가면 false
            return -1
            
    return -1

input = sys.stdin.readline
T = int(input())
for _ in range(T):

    M, N, x, y = map(int, input().split())
    a, b = 1, 1
    if x==1 and y==1:
        print(1)
    else:
        print(solve(a, b))

# git commit -m "code: Solve boj 06064 카잉 달력 (seungkyu)"