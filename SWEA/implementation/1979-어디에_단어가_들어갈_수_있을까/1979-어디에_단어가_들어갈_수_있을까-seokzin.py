T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())

    arr = [list(map(int, input().split())) + [0] for _ in range(N)]
    arr.append([0]*(N+1))  # 0을 더해주는 이유 - 끝값이 1이면 else문을 통해 cnt 검증을 하지 못해서

    res = 0

    for a in range(N):
        cnt = 0

        for b in range(N+1):  # 가로 순회
            if arr[a][b]:
                cnt += 1

            else:
                if cnt == K:
                    res += 1
                cnt = 0

        for b in range(N+1):  # 세로 순회
            if arr[b][a]:
                cnt += 1
            else:
                if cnt == K:
                    res += 1
                cnt = 0

    print(f"#{tc} {res}")

# 예전에 푼 코드로 대체하겠습니다.
# 모든 좌표를 순회하며 카운팅을 하고, 벽을 만나면 초기화하는 형태