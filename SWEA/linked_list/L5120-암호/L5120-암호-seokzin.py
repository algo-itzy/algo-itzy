for tc in range(1, int(input())+1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    idx = 0

    for _ in range(K):
        nxt = (idx+M) % len(arr)  # nxt = next
        if nxt == 0:  # 이거 처리때문에 너무 지저분해졌다.....
            arr.append(arr[nxt-1] + arr[nxt])
            nxt -= 1
        else:
            arr.insert(nxt, arr[nxt-1] + arr[nxt])

        idx = nxt

    print(f'#{tc}', *arr[::-1][:10])

# insert 첫번째 인자 값이 list 크기를 넘으면 안된다..