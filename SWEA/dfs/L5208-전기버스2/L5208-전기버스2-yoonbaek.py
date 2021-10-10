def back_track(cnt, idx):
    global min_cnt

    if cnt >= min_cnt:
        return

    if idx >= N:
        min_cnt = cnt
        return

    for i in range(idx+infos[idx], idx, -1):
        back_track(cnt+1, i)


if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T+1):
        infos = list(map(int, input().split()))
        N = infos[0]
        min_cnt = 100

        back_track(0, 1)

        print(f"#{tc} {min_cnt-1}")
# git commit -m "code: Solve swea L5208 전기버스2 (yoonbaek)"