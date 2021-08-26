import sys
sys.stdin = open('input.txt')
# 중위 탐색 방식? heap으로 풀었는데 아예 틀림

def make_b_tree(idx):
    global cnt
    if idx <= N:
        make_b_tree(idx*2)  # 왼쪽 자식노드
        b_tree[idx] = cnt  # 값 입력
        cnt += 1
        make_b_tree(idx*2 + 1)  # 오른쪽 자식노드

T = int(input())
for test_case in range(1, T+1):

    N = int(input())
    b_tree = [0]*(N+1)
    cnt = 1
    make_b_tree(1)
    print(f'#{test_case} {b_tree[1]} {b_tree[N//2]}')
