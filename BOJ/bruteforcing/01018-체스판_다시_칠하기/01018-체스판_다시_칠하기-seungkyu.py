'''
8x8 검사 후 한 칸씩 이동
8x8 matrix를 오른쪽으로 한칸 씩 이동하면 체크,
끝에 다다르면 열 처음 값으로 바꾼 뒤 행 한 칸 밑으로 이동
생각 못했던 점 - 현재 행의 번호 + 현재 열의 번호 합이 
짝수이면 시작점의 색깔과 같아야 하고,
홀수이면 시작점의 색깔과 다른 색이어야 한다.
'''
import sys

def input_func():
    # list로 감쌀 필요 없음
    n, m = map(int, input().split())
    mat = []
    for _ in range(n) :
        mat.append(sys.stdin.readline().rstrip())

    return mat, n, m

def solve(mat, n, m) :
    
    answer = [] # 한 번 체크 시 최소변화 횟수 저장할 리스트

    col_start = row_start = 0 # 열 시작점, 끝 점
    col_end = row_end = 8 # 행 시작점, 끝 점

    while 1 :
        cnt_to_w = 0 # W로 바꾸는 횟수
        cnt_to_b = 0 # B로 바꾸는 횟수
        if row_end == n+1 : 
            break
        for row_idx in range(row_start, row_end) :
            for col_idx in range(col_start, col_end) :

                # 1. 왼쪽 위끝 W로 시작
                # 2. 왼쪽 위끝 B로 시작

                if (row_idx + col_idx) % 2 == 0 : # 시작점의 색깔과 같아야 함
                    if mat[row_idx][col_idx] != 'W' : # 1. W가 와야하는 자리
                        cnt_to_w += 1
                    if mat[row_idx][col_idx] != 'B' : # 2. B가 와야하는 자리
                        cnt_to_b += 1
                else : # 시작점의 색깔과 다른 색이어야 함
                    if mat[row_idx][col_idx] != 'B' : # 1. B가 와야하는 자리
                        cnt_to_w += 1
                    if mat[row_idx][col_idx] != 'W' : # 2. W가 와야하는 자리
                        cnt_to_b += 1

        answer.append(min(cnt_to_w, cnt_to_b)) # 둘 중 최소값만 저장
        col_start += 1
        col_end += 1

        if col_end == m+1 : # 오른쪽 끝에 다다랐을 경우
            col_start = 0 # 열 처음 위치로
            col_end = 8
            row_start += 1 # 행 한칸 밑으로 이동
            row_end += 1

    print(min(answer))

if __name__ == '__main__' :
    mat, n, m = input_func()
    solve(mat, n, m)

'''
예전 코드
if row_idx % 2 == 0 and col_idx % 2 == 0 : # 홀수 행, 홀수 열
  
elif row_idx % 2 == 0 and col_idx % 2 == 1 : # 홀수 행, 짝수 열
 
elif row_idx % 2 == 1 and col_idx % 2 == 0 : # 짝수 행, 홀수 열

elif row_idx % 2 == 1 and col_idx % 2 == 1 : # 짝수 행, 짝수 열

'''
