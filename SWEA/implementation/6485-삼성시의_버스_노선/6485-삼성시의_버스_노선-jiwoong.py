"""
# 삼성시의 버스 노선
P개의 버스 정류장에 대해 각 정류장에 몇 개의 버스 노선이 다니는지

첫 번째 줄에 테스트 케이스의 수 T
각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N
다음 N개의 줄의 i번째 줄에는 두 정수 Ai, Bi, 공백 하나로 구분
다음 줄에는 하나의 정수 P
다음 P개의 줄의 j번째 줄에는 하나의 정수 Cj

각 테스트 케이스마다 ‘#x' 를 출력, 한 칸을 띄운 후,
한 줄에 P개의 정수를 공백 하나 구분하여 출력
j번째 정수는 Cj번 버스 정류장을 지나는 버스 노선의 개수
"""

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    bus = [0] * 5001

    for i in range(N):
        Ai, Bi = map(int, input().split())
        for j in range(Ai, Bi + 1):
            bus[j] += 1
    P = int(input())
    ans = []

    for i in range(P):
        ans.append(int(input()))

    for i in range(len(ans)):
        ans[i] = str(bus[ans[i]])
    print('#{} {}'.format(tc, ' '.join(ans)))