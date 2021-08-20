def rotate(arr):
    
    new_arr = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_arr[j][n-i-1] = arr[i][j] # 오른쪽 방향으로 90도씩 회전하여 새 배열에 담기 
    return new_arr

t = int(input())

for tc in range(t):
    n = int(input())

    arr_input = [list(map(int, input().split())) for _ in range(n)] 
    
    ans90 =rotate(arr_input)
    ans180 = rotate(ans90)
    ans270 = rotate(ans180)

    print(f'#{tc+1}')
    for i in range(n):
        print("".join(map(str, ans90[i])), end=' ')
        print("".join(map(str, ans180[i])), end = ' ')
        print("".join(map(str, ans270[i])))

