for test in range(1,int(input())+1):
    N, M = map(int, input().split())
    arr = [float('inf')]
    cnt = 0
    for _ in range(M):
        a = list(map(int, input().split()))
        for i in range(N*cnt+1):
            if a[0] < arr[i]:
                arr[i:i] = a
                break
        cnt +=  1
    print(f'#{test}',end=' ')
    print(*arr[-11:-1][::-1])