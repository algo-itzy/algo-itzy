import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    # 가로줄, 세로줄 검사시 맨 뒤칸이 1일 때 체크가 잘 안되는 거 같아서
    # 가로줄 끝, 세로줄 끝에 0을 추가로 넣어주는 작업을 한 뒤 풀었습니다.
    '''
    1 1 1 1 1 + 0
    1 1 1 1 1 + 0
    1 1 1 1 1 + 0
    1 1 1 1 1 + 0
    1 1 1 1 1 + 0
    + + + + +
    0 0 0 0 0
    '''
    matrix = [list(map(int, input().split()))+[0] for _ in range(N)] + [[0 for _ in range(N)]]
    ans = 0

    # 가로줄 검사
    for i in range(N):
        length = cnt = 0
        for j in range(N+1):
            if matrix[i][j]:  # 1이 계속해서 나오면 길이+1
                cnt += 1
                length = cnt
            else:  # 0이 나오면 지금까지 계산한 길이로 check
                cnt = 0
                if length == K:  # K길이 찾으면 ans+1
                    length = 0
                    ans += 1

    # 세로줄 검사 (가로줄 검사와 동일, 인덱스만 다름)
    for j in range(N):
        length = cnt = 0
        for i in range(N+1):
            if matrix[i][j]:
                cnt += 1
                length = cnt
            else:
                cnt = 0
                if length == K:
                    length = 0
                    ans += 1

    print(f'#{test_case} {ans}')
