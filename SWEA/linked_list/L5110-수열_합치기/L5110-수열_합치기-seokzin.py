for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    res = []
    
    for _ in range(M):
        arr = list(map(int, input().split()))

        for i in range(len(res)):
            if res[i] > arr[0]:
                res[i:i] = arr  # 얘는 Pass
                # res = res[:i] + arr + res[i:]  # 얘는 시간초과
                break
        else:
            res += arr  # for문 통과시 맨 뒤에 extend

    print(f'#{tc}', *res[-1:-11:-1])  # 뒤집어서 10개 출력 어떻게 더 잘하지