t = int(input())

for tc in range(t):
    n, m = map(int, input().split())                # 수열의 길이 n, 수열의 개수 m
    
    base = list(map(int, input().split()))          # 맨 위의 수열을 기준으로, 그 수열에 원소들을 추가해나갈 것

    for i in range(0, m-1):                         # 그 나머지 수열들
        suyeol = list(map(int, input().split()))    # m 개의 줄에 걸쳐 수열을 입력 받음

        for j in range(len(base)):
            if base[j] > suyeol[0]:
                base[j:j] = suyeol                  # base 수열의 j 번째 자리에 붙여넣음
                break 
        else: 
            base += suyeol 
        
    print(f'#{tc+1}', *base[-1:-11:-1])
    
    