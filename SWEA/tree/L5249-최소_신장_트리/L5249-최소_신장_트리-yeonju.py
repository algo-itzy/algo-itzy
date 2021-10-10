# 2차시의 프림 알고리즘 수도코드 조금만 변형해서 풀었습니다.

t = int(input())

for tc in range(t):
    v, e = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(e)]
    # n1, n2, w

    key = [float("inf")] * (v+1)
    visited = [0] * (v+1)
    key[arr[0][0]] = 0
    # key[0] = 0

    for _ in range(v+1):
        minimum = float("inf")

        for i in range(v+1):
            if not visited[i] and key[i] < minimum:
                minimum = key[i]
                minindex = i
        visited[minindex] = True

        for i in range(e):      # 무향 그래프여서 arr[i][0]과 arr[i][1] 을 둘 다 해주기
            if arr[i][0] == minindex:
                node = arr[i][1]
                val = arr[i][2]
                if not visited[node] and val < key[node]:
                    key[node] = val

            if arr[i][1] == minindex:
                node = arr[i][0]
                val = arr[i][2]
                if not visited[node] and val < key[node]:
                    key[node] = val
    res = sum(key)
    print("#{} {}".format(tc+1,res))

# git commit -m "code: Solve swea L5249 최소 신장 트리 (yeonju)"