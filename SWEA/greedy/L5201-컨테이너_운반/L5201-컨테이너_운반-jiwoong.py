# git commit -m "code: Solve swea L5201 컨테이너 운반 (jiwoong)"
T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N: 컨테이너수, M: 트럭수
    weight = sorted(list(map(int, input().split())), reverse=True)  # N개의 화물 무게
    truck = sorted(list(map(int, input().split())), reverse=True)  # M개 트럭의 적재용량

    ans = 0
    cnt = 0
    i, j = 0, 0  # truck, weight
    while True:
        if cnt == min(N, M):
            break
        if truck[i] >= weight[j]:
            ans += weight[j]
            i += 1
            j += 1
        else:
            j += 1
        cnt += 1

    print("#{} {}".format(tc, ans))
