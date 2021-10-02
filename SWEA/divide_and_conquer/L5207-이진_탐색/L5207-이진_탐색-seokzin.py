def binary_search(x):
    s, e = 0, n-1
    flag = ''

    while s <= e:
        m = (s+e) // 2
    
        if a[m] < x:
            s = m+1  # 오른쪽 구간 선택
            
            if flag == 'r':
                return 0
            else:
                flag = 'r'
                
        elif a[m] > x:
            e = m-1  # 왼쪽 구간 선택

            if flag == 'l':
                return 0
            else:
                flag = 'l'

        elif a[m] == x:
            return 1

    return 0


for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    a = sorted(list(map(int,input().split())))
    b = list(map(int, input().split()))

    print(f'#{tc}', sum(map(binary_search, b)))

# 신선한 문제였습니다.