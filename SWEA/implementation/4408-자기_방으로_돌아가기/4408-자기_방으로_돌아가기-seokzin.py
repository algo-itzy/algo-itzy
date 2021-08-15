T = int(input())

for tc in range(1, T+1):
    N = int(input())
    
    corridor = [0] * 200  # 복도 배열

    for _ in range(N):
        A, B = sorted(map(int,input().split()))

        a = A//2 if A%2 == 1 else A//2 - 1  # 좌표 보정
        b = B//2 if B%2 == 1 else B//2 - 1

        for i in range(a, b+1):
            corridor[i] += 1

    print(f'#{tc}', max(corridor))

# [10--------------100]
#    [20--------80]
#       [30--50]

# 최고 깊이는 3 - 4836 색칠하기 응용
# A, B 사전 정렬을 해줘야해서 map에 sorted를 써보니까 잘 됐다. 신기