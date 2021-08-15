import sys
input = sys.stdin.readline

def check(x,y,matrix):
    col_check_box = {i:False for i in range(1,10)}
    row_check_box = {i:False for i in range(1,10)}
    box_check = {i:False for i in range(1,10)}
    # 행 검사
    for num in matrix[x]:
        if not col_check_box[num]:
            col_check_box[num] = True
        else:
            return False
    # 열 검사
    for j in range(9):
        num = matrix[j][y]
        if not row_check_box[num]:
            row_check_box[num] = True
        else:
            return False
    # 박스 검사
    for i in range(3):
        for j in range(3):
            num = matrix[(x+i)%3][(y+j)%3]
            if not box_check[num]:
                box_check[num] = True
            else:
                return False
    return True

def check_sudoku(s):
    # 0,0에서 1,3씩 늘려가며 8이상 넘어가면 8로 나눈 나머지로 바꿔줌 총 9번 검사.
    i = 0
    for j in range(0,24,3):
        if check(i,j%8,s):
            i += 1
        else:
            return 0
    else:
        return 1 if check(8,8,s) else 0



for test in range(1,int(input())+1):
    sudoku = [list(map(int,input().split())) for _ in range(9)]
    print(f'#{test} {check_sudoku(sudoku)}') 