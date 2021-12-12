import heapq
import sys

INF = sys.maxsize
input = sys.stdin.readline


def dijkstra(graph, start):

    distances = [INF] * len(graph)
    distances[start] = 0

    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        current_distance, current_destination = heapq.heappop(queue)

        if distances[current_destination] < current_distance:
            continue

        for new_destination, new_distance in graph[current_destination]:
            distance = current_distance + new_distance

            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, (distance, new_destination))


    return distances


n, m, x = map(int, input().split())

graph = [[] for i in range(n+1)]

for i in range(m):
    start, end, time = map(int, input().split())
    graph[start].append((end, time))


round_trip = []
to_home = dijkstra(graph, x)

for i in range(1, n+1):

    to_party = dijkstra(graph, i)
    round_trip.append(to_party[x]+ to_home[i])

print(max(round_trip))

# git commit -m "code: Solve boj 01238 파티 (yeonju)"