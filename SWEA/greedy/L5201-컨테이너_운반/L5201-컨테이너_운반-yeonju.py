def check():
    total = 0                              # 옮겨진 화물 전체 무게
    while truck and container:
        if truck[-1] >= container[-1]:       # 컨테이너가 트럭에 담기면
            tmp = container.pop()
            total += tmp
            truck.pop()

        else:                              # 컨테이너가 트력에 안 담기면(컨테이너가 더 큰 경우)
                                        # 트럭에 안 담기는 컨테이너는 버리기
            container.pop()

    return total


t = int(input())

for tc in range(t):
    n, m = map(int, input().split())                # 컨테이너 수, 트럭 수
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    container = sorted(container)      # 오름차순 정렬 후 큰 순서대로 앞에 오도록 재배치
    truck = sorted(truck)

    print(f'#{tc+1} {check()}')


# git commit -m "code: Solve swea L5201 컨테이너 운반 (yeonju)"
