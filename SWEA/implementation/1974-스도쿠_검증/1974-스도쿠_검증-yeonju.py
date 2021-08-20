def check_square(v):
    x, y = v
    box = [0] * 10
    box[0] = 1
    for i in range(3):          # 3 x 3 박스 안에 1~9 모두 있나 확인  
        for j in range(3):
            box[arr[x+i][y+j]] = 1

    res = 1
    for i in box:
        if i != 1:
            res = 0
            break
    
    return res

def check_vertical(v2):

    x,y = v2 # 0,i
    box2 = [0] * 10
    box2[0] = 1

    for i in range(9):
        box2[arr[x+i][y]] = 1
    
    res = 1

    for i in box2:
        if i != 1:
            res = 0 
            break
    
    return res

def check_horizontal(v2):
    x,y = v3 # i,0
    box3 = [0] * 10
    box3[0] = 1

    for i in range(9):
        box3[arr[x][y+i]] = 1

    res = 1

    for i in box3:
        if i != 1:
            res = 0
            break
    
    return res


t = int(input()) # 테스트 케이스 개수 T 

for tc in range(t):
    arr = [list(map(int, input().split())) for _ in range(9)] # 리스트에 스도쿠 값들 입력 받기 
    
    total = 0
    
    for i in range(3):      # 3x3 의 맨 위 왼쪽 원소들을 따로 빼와서, check() 함수에 넣기
        for j in range(3):
            v = [3*i, 3*j] 
            total += check_square(v)
            


    for i in range(9):      # 세로로 체크
            v2 = [0,i]
            total += check_vertical(v2)

    for i in range(9): # 가로로 체크
            v3 = [i,0]
            total += check_horizontal(v3)

    if total ==27:
        answer = 1
    else: 
        answer = 0
    
    print(f'#{tc+1} {answer}')
