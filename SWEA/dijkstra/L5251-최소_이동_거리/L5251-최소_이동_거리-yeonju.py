# 5차시의 다익스트라 알고리즘 수도코드 조금 변형해서 풀었습니다.

t = int(input())

for tc in range(t):
    n, e = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(e)]

    key = [float("inf")] * (n+1)
    visited = [0] * (n+1)
    key[arr[0][0]] = 0
    # key[0] = 0

    for _ in range(n+1):
        minimum = float("inf")

        for i in range(n+1):
            if not visited[i] and key[i] < minimum:
                minimum = key[i]
                minindex = i
        visited[minindex] = True

        for i in range(e):

            if arr[i][0] == minindex:
                node = arr[i][1]
                val = arr[i][2]
                if not visited[node] and key[minindex] + val < key[node]: # 여태까지 온 거리를 다 더해주는 것이 프림 알고리즘과의 차이점
                    key[node] = key[minindex] + val

    res = key[-1]
    print("#{} {}".format(tc+1, res))


# git commit -m "code: Solve swea L5251 최소 이동 거리 (yeonju)"