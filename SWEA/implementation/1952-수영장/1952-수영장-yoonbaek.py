if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T+1):
        day, mon, qtr, yr  = map(int, input().split())
        plans = [0] + list(map(int, input().split()))
        totals = [0] * 13

        for i, plan in enumerate(plans):
            plans[i] = min(day*plan, mon)

        for i, plan in enumerate(plans):
            totals[i] = totals[i-1] + plan
            if i >= 3:
                if totals[i] > totals[i-3] + qtr:
                    totals[i] = totals[i-3] + qtr

        if totals[-1] > yr:
            totals[-1] = yr

        print(f"#{tc} {totals[-1]}")

# git commit -m "code: Solve swea 1952 수영장 (yoonbaek)"