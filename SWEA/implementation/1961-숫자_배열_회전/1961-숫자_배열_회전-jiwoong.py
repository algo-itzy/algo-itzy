"""
# 숫자 배열 회전
N x N 행렬이 주어질 때, 시계 방향으로 90도, 180도, 270도 회전한 모양을 출력

첫 줄에 테스트 케이스의 개수 T, 그 아래로 각 테스트 케이스
각 테스트 케이스의 첫 번째 줄에 N
다음 N 줄에는 N x N 행렬

출력의 첫 줄은 '#t '로 시작
다음 N줄에 걸쳐서 90도, 180도, 270도 회전한 모양을 출력
회전한 모양 사이에만 공백
"""

T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 행렬의 수
    arr = [[[0] * N for _ in range(N)] for _ in range(4)]
    for i in range(N):
        arr[0][i] = list(map(int, input().split()))

    # 회전
    for k in range(1, 4):
        for i in range(N):
            for j in range(N):
                arr[k][j][N-1-i] = arr[k-1][i][j]

    # 출력
    print(f"#{tc}")
    for i in range(N):
        for k in range(1, 4):
            if k != 1: print(end = " ")
            for j in range(N):
                print(arr[k][i][j], end = "")
        print()