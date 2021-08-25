T = int(input())
for tc in range(1, T + 1):
    N, K, M = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = 0
    for i in range(M):
        ans += K
        ans = ans % len(arr)
        if ans == 0:
            arr.append(arr[0] + arr[-1])
            ans -= 1
        else:
            arr.insert(ans, arr[ans - 1] + arr[ans])
    if len(arr) > 10:
        print(f"#{tc}", end=' ')
        for i in range(1, 11):
            print(arr[-i], end=' ')
        print()
    else:
        print(f"#{tc}", end=' ')
        for i in range(1, len(arr) + 1):
            print(arr[-i], end=' ')
        print()
