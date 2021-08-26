import sys
sys.stdin = open('input.txt')


def get_tree(n):
    global cnt

    if n <= N:
        # 왼쪽 자식 노드는 현재 노드 인덱스의 두배
        get_tree(n*2)
        tree[n] = cnt
        cnt += 1
        # 오른쪽 자식 노드는 현재 인덱스 두배 + 1
        get_tree(n * 2 + 1)


for t in range(1, int(input())+1):
    N = int(input())
    tree = [0] * (N+1)
    cnt = 1
    get_tree(1)
    print(f"#{t}", tree[1], tree[N//2])  # 루트, N/2번 노드

"""
구글링으로 꾸역꾸역... ㅠㅠ
"""
