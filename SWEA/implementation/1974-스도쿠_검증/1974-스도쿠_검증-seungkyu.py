import sys
sys.stdin = open('input2.txt')

T = int(input())

for test_case in range(1, T+1):

    sudoku = [list(map(int, input().split())) for _ in range(9)]
    sudoku_t = list(zip(*sudoku))  # 세로 검증하기 위해 선언

    ans = 1
    cnt = 0
    # 왼쪽 블록, 가운데 블록, 오른쪽 블록 만들어서 검사
    left_list, center_list, right_list = [], [], []

    # 가로줄 검사
    for row in sudoku:
        if len(set(row)) != 9:  # 숫자 중복 제거후 9개인지 확인
            ans = 0
            break
        # 블록 단위 검사 row를 3개씩 끊어서 검사하기위해 cnt 사용
        if cnt < 3:
            left_list += (row[0:3])
            center_list += (row[3:6])
            right_list += (row[6:9])
            cnt += 1
        if cnt == 3:  # row가 3개 모였을 때 검사
            if len(set(left_list)) != 9 or len(set(center_list)) != 9 or len(set(right_list)) != 9:
                ans = 0
                break
            # 왼쪽 블록, 가운데 블록, 오른쪽 블록 리셋
            left_list, center_list, right_list = [], [], []
            cnt = 0  # cnt 리셋
            
    if ans:  # 가로줄에서 이상없었으면 이어서 검사
        # 세로줄 검사
        for col in sudoku_t:
            if len(set(col)) != 9:
                ans = 0
                break

    print(f'#{test_case} {ans}')
