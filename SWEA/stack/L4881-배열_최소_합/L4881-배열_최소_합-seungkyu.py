import sys
sys.stdin = open('input.txt')

def solve(row, sum_num):
    global min_num  #  답 저장
    # 중간에 최솟값을 넘었을 때 종료
    if sum_num > min_num:
        return

    # 모든 row를 돌았을 때 답 업데이트
    if row == N:
        if sum_num < min_num:
            min_num = sum_num
        return min_num

    for col in range(N):
        if not visited[col]:  # 방문하지 않은 col일 경우 방문
            visited[col] = 1
            solve(row+1, sum_num+matrix[row][col])  # 행 증가해서 반복
            visited[col] = 0  # 방문한 것 취소


T = int(input())

for test_case in range(1, T+1):

    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    min_num = 9*N  # 최대 가능값(9) * N개로 최댓값 설정
    visited = [0]*N
    sum_num = 0
    solve(0, 0)

    print(f'#{test_case} {min_num}')
