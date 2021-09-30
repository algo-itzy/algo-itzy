key = lambda x: (x[1], x[0])

if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T+1):
        N = int(input())
    
        schedules = sorted([tuple(map(int, input().split())) for _ in range(N)], key=key)
        
        cnt = 0
        prev = 0
        for start, end in schedules:
            if prev <= start:
                cnt += 1
                prev = end

        print(f"#{tc} {cnt}")

# git commit -m "code: Solve swea L5202 화물 도크 (yoonbaek)"