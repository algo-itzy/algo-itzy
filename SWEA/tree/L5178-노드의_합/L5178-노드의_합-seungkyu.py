import sys
sys.stdin = open('input.txt')


def sum_child():
    for i in range(N, 0, -1):  # 뒤에서 부터 진행
        if i//2:  # 부모노드가 있을 때
            tree[i//2] += tree[i]  # 부모노드에 자식 값 더하기


T = int(input())
for test_case in range(1, T+1):

    N, M, L = map(int, input().split())
    tree = [0]*(N+1)
    for _ in range(M):
        a, b = map(int, input().split())
        tree[a] = b

    sum_child()
    print(f'#{test_case} {tree[L]}')
