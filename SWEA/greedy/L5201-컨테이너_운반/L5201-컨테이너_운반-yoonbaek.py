if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T+1):
        N, M = map(int, input().split())
        containers = sorted(list(map(int, input().split())), reverse=True)
        trucks = sorted(list(map(int, input().split())), reverse=True)

        total, c, t = 0, 0, 0
        while c < N and t < M:
            if containers[c] <= trucks[t]:
                total += containers[c]
                t += 1
            c += 1
    
        print(f"#{tc} {total}")

# git commit -m "code: Solve swea L5201 컨테이너 운반 (yoonbaek)"