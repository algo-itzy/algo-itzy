def rotate(arr):  # 90도 회전
    new_arr = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            new_arr[j][N-1-i] = arr[i][j]

    return new_arr


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    arr_90 = rotate(arr)
    arr_180 = rotate(arr_90)
    arr_270 = rotate(arr_180)
    
    print(f'#{tc}')
    for i in range(N):
        print(*arr_90[i], ' ', *arr_180[i], ' ', *arr_270[i], sep='')

# 생각보다 출력부가 까다롭네요.