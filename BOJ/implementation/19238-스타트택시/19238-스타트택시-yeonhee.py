import sys
input = sys.stdin.readline

N, M, fuel = map(int, input().split())

area = [[1 for _ in range(N + 1)]]
for _ in range(N):
    area.append([1])
    area[-1].extend(list(map(int, input().split())))

now = tuple(map(int, input().split()))

passenger = {}
for _ in range(M):
    a, b, c, d = map(int, input().split())
    passenger[(a, b)] = (c, d)

DIRECTIONS = ((0, 1), (1, 0), (-1, 0), (0, -1))

# Flag
take_a_taxi = False

while passenger:
    arrival, target = tuple(), set()
    visited, queue = set(), {now}
    move = 0
    while queue:
        candidate = set()
        for r, c in queue:
            if (0 <= r < N+1 and 0 <= c < N+1) and not area[r][c]:
                if take_a_taxi and (r, c) == passenger[now]:
                    del passenger[now]
                    arrival = (r, c)
                    break

                elif not take_a_taxi and (r, c) in passenger:
                    target.add((r, c))

                else:
                    for dr, dc in DIRECTIONS:
                        nr, nc = r + dr, c + dc
                        if (nr, nc) not in visited:
                            candidate.add((nr, nc))

            visited.add((r, c))

        if arrival:
            take_a_taxi = False
            now = arrival
            fuel = fuel + move if fuel >= move else -1
            break

        if target:
            take_a_taxi = True
            now = sorted(target)[0]
            fuel -= move
            break

        if not candidate:
            fuel = -1
            break

        queue = candidate
        move += 1

    if fuel < 0:
        fuel = -1
        break

print(fuel)
