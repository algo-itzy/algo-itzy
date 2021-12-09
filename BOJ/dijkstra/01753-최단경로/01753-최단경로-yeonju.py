import heapq

graph = {
    'A': {'B': 10, 'C': 3},
    'B': {'C': 1, 'D': 2},
    'C': {'B': 4, 'D': 8, 'E': 2},
    'D': {'E': 7},
    'E': {'D': 9},
}


def dijkstra(start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    queue = []
    heapq.heappush(queue, [distances[start], start]) # 우선순위 큐에 시작 노드 a 의 거리를 추가

    while queue:
        current_distance, node = heapq.heappop(queue)

        if distances[node] < current_distance:
            continue

        for new_destination, new_distance in graph[node].items():
            distance = current_distance + new_distance

            if distance < distances[new_destination]:
                distances[new_destination] = distance

                heapq.heappush(queue, [distance, new_destination])

    return distances


print(dijkstra('A'))


# git commit -m "code: Solve boj 01753 최단경로 (yeonju)"