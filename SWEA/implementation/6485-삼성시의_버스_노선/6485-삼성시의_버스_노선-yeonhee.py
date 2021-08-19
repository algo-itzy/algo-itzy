import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    # 버스정류장 초기화
    bus_stop = [0 for _ in range(5001)]

    # 버스 노선
    for _ in range(int(input())):
        a, b = map(int, input().split())
        for i in range(a, b+1):
            bus_stop[i] += 1

    # 출력할 버스 정류장
    result = [bus_stop[int(input())] for _ in range(int(input()))]

    print(f'#{t}', *result)
