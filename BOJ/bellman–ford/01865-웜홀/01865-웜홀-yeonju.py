# 블로그 풀이 참조했습니당,,, ㅇ_ㅇ (거의 그대로 ㄱ..ㅏ져...왔....다고 해도 무...방....)

def bel(start):
    distance[start] = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            for next, time in graph[j]:
                if distance[next] > distance[j] + time:
                    distance[next] = distance[j] + time
                    if i == n:
                        return True

    return False


tc = int(input())

for _ in range(tc):
    n, m, w = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    distance = [10001 for _ in range(n+1)]
    for _ in range(m):
        s, e, t = map(int, input().split()) # s-e 연결, t- 이동 시간
        graph[s].append([e, t])
        graph[e].append([s, t])
    for _ in range(w):
        s, e, t = map(int, input().split())
        graph[s].append([e, -t])

    negative_cycle = bel(1)
    if not negative_cycle:
        print('NO')
    else:
        print('YES')

# git commit -m "code: Solve boj 01865 웜홀 (yeonju)"