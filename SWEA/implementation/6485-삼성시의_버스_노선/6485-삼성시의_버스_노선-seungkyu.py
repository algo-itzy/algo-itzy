import sys
sys.stdin = open('s_input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())  # 버스 노선 수

    bus_stop_ranges = []
    for _ in range(N):
        bus_stop_ranges.append(list(map(int, input().split())))
    P = int(input())  # 정류장 개수

    bus_stops = []
    for _ in range(P):
        bus_stops.append(int(input()))

    ans = [0]*P  
    for bus_stop_range in bus_stop_ranges:  # 주어진 버스를 차례대로 돌면서 check
        for idx, stop in enumerate(bus_stops):
            # 버스가 다니는 범위안의 정류장들 모두 업뎃(누적)
            if bus_stop_range[0] <= stop <= bus_stop_range[1]:
                ans[idx] += 1  # 누적

    print(f'#{test_case}', end=' ')
    print(*ans)
