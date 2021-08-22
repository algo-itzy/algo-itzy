T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    queue = []
    for n in range(N):
        queue.append(arr[n])
        # queue 에 arr 값 삽입
    for m in range(M):
        first = queue.pop(0)
        queue.append(first)

    print("#{} {}".format(tc, queue[0]))