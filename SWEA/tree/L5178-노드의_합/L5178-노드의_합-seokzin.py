for tc in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+2)  # try except 처리하기 싫어서 빈 리프를 하나 더 채움	

    for _ in range(M) :					
        a, b = map(int, input().split())		
        tree[a] = b

    for i in range(N-M, 0, -1) :
        tree[i] = tree[i*2] + tree[i*2+1]
    
    print(f'#{tc}',tree[L])
