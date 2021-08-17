"""
# 자기 방으로 돌아가기
최단 시간에 모든 학생이 자신의 방으로
숙소는 긴 복도를 따라 총 400개의 방 배열
만약 두 학생이 돌아가면서 지나는 복도의 구간이 겹치면 두 학생은 동시에 돌아갈 수 없다.
한 사람은 기다렸다가 다음 차례에 이동
각 학생들의 현재 방 위치와 돌아가야 할 방의 위치의 목록이 주어질 때,
최소 몇 단위시간만에 모든 학생들이 이동할 수 있는지

입력은 T(≤10)개의 테스트 케이스
각 테스트 케이스의 첫 줄에는 돌아가야 할 학생들의 수 N
다음 N 줄에는 각 학생의 현재 방 번호와 돌아가야 할 방의 번호

테스트 케이스 T에 대한 결과는 “#T ”을 찍고, 각 테스트 케이스마다 필요한 시간을 한 줄에 하나씩 출력
"""

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    togo = [list(map(int, input().split())) for _ in range(N)]

    rooms = [0] * 200

    for i, j in togo:
        left = (i - 1) // 2
        right = (j - 1) // 2

        if right >= left:
            for k in range(left, right + 1):
                rooms[k] += 1
        else:
            for k in range(right, left + 1):
                rooms[k] += 1

    ans = 0
    for room in rooms:
        if room > ans:
            ans = room

    print(f'#{tc} {ans}')
