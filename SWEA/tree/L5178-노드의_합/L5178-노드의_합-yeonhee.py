import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+2)

    for _ in range(M):
        idx, num = map(int, input().split())
        tree[idx] = num

    for i in range(N-M, 0, -1):
        tree[i] = tree[i*2] + tree[i*2 + 1]

    print(f'#{t} {tree[L]}')
