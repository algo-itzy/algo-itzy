t = int(input())

for tc in range(t):
    n, m , l = map(int, input().split())
    suyeol = list(map(int, input().split()))

    for i in range(m):
        info = list(input().split())

        if info[0] == 'I':
            suyeol.insert(int(info[1]), int(info[2]))   # 해당 번째 인덱스 앞에 원소 추가

        elif info[0] == 'D':
            suyeol.pop(int(info[1]))                    # 해당 인덱스의 값만 빼기 + 뒤에 있는 원소들은 앞으로 붙이기 

        elif info[0] =='C':
            suyeol[int(info[1])] = int(info[2])         # 해당 인덱스의 값을 변경 
        
    if len(suyeol) > l:                                 # l 번째 원소가 있으면 
        print(f'#{tc+1} {suyeol[l]}')
    else:
        print(f'#{tc+1} -1') 
    

