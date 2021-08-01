import sys
input = sys.stdin.readline

coordinates = []

for _ in range(int(input())):
    coordinates.append(list(map(int, input().split())))

coordinates.sort(key = lambda x: (x[0], x[1]))

for x, y in coordinates:
    print(x, y)
    