t = int(input())

for tc in range(t):
    n, m, l = map(int, input().split()) # 수열의 길이 n, 추가 횟수 m, 출력할 인덱스 번호 l
    suyeol = list(map(int, input().split()))
    for i in range(m):
        index, num = map(int, input().split())
        suyeol.insert(index, num) # 해당되는 인덱스의 자리에 num를 insert 
    
    print(f'#{tc+1} {suyeol[l]}') 
