for test in range(1,int(input())+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    print(f'#{test} {arr[M%N]}')