for test in range(1,int(input())+1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    i = M
    for _ in range(K):
        i %= N
        if not i:
            arr.append(arr[-1]+arr[0])
            i -= 1
        else:
            arr.insert(i,arr[i-1]+arr[i])
        N += 1
        i += M
    print(f'#{test}', end=' ')
    print(*arr[-10:][::-1])