import sys
sys.stdin = open('input.txt')


def min_heap(data):  # 데이터 힙으로 만들기
    # 들어온 숫자를 tree 리스트에 넣고
    tree.append(data)

    # 현재 인덱스 설정 (tree 가 0으로 시작해서)
    idx = len(tree) - 1

    while idx > 1:
        # parent_index
        p_idx = idx//2

        # 만약 부모 노드가 더 크면 자식 노드랑 위치 변경
        if tree[p_idx] > tree[idx]:
            tree[p_idx], tree[idx] = tree[idx], tree[p_idx]

        # 부모 단계로 올라감
        idx = p_idx


def get_sum():  # 마지막 노드의 조상들의 합
    result = 0
    idx = N

    while idx:
        idx //= 2
        result += tree[idx]

    return result


for t in range(1, int(input())+1):
    answer = 0
    N = int(input())
    numbers = list(map(int, input().split()))
    tree = [0]

    for num in numbers:  # 힙으로 변환해서 tree 에 넣기
        min_heap(num)

    print(f'#{t} {get_sum()}')
