T= int(input()) # 테스트 케이스 개수 T
   
for tc in range(T):
    n = int(input()) #20 x N 크기 (N은 10의 단위!)

    n= n//10        # 한 칸이 10 긴 하지만, 1 만큼씩 늘어난다고 생각 
    
    li = [0] * n    # 리스트를 미리 생성해서 값을 차곡차곡 
    
    li[0] = 1       # 상자의 가로가 10 cm 인 경우
    li[1] = 3       # 상자의 가로가 20cm 로 넣을 수 있는 박스 개수

    if n >= 2: 
        for i in range(2, n):
            li[i] = li[i-1] + 2 * li[i-2]
        
    print(f'#{tc+1} {li[n-1]}')


    