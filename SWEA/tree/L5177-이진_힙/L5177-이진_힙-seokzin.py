def heapify(x):
    tree.append(x)  # 인덱스 마지막에 넣기
    idx = len(tree)-1

    while idx > 1 and tree[idx] < tree[idx//2]:  # 부모보다 작으면 교환 작업 (루트 아니고)
        tree[idx], tree[idx//2] = tree[idx//2], tree[idx]
        idx //= 2


def sum_tree():  # 마지막 요소부터 루트 합
    idx = len(tree)-1
    res = 0

    while idx > 1:
        res += tree[idx//2]
        idx //= 2
    
    return res


for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))  # 힙정렬
    tree = [0]  # 인덱스 0은 더미로 채움

    for x in arr:  # 요소 넣고 힙정렬 계속 반복
        heapify(x)

    print(f'#{tc}', sum_tree())

# heapify를 직접 구현할 수 있어서 어렵지만 재밌었던 문제!