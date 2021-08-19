t = int(input())

for tc in range(t):
    n = int(input())                                          # 버스 노선 개수 n

    ab = [list(map(int, input().split())) for _ in range(n)]  # ex) 1 3
                                                              # 1,2,3 정류장을 다니는 버스 노선

    p = int(input())                                          # 몇개의 노선이 다니는지 구해야할 정류장 수 p

    c = [int(input()) for _ in range(p)]                      # c 정류장에 다니는 노선 수를 구해야 함 

    bus = []                                                  # c 정류장들을 다니는 노선 수를 담을 리스트 bus 선언  
    for c_each in c:
        cnt = 0                     
        for a, b in ab:                                       # a,b 의 노선이 c 정류장을 지나면 카운트
            if a <= c_each <= b:
                cnt += 1

        bus.append(cnt)

    print(f'#{tc+1}', *bus)
