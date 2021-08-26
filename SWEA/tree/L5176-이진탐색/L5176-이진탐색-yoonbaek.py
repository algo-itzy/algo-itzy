def make_bin_tree(start):
    global cnt

    if start <= N:
        # 왼쪽 자식 노드 규칙성 재귀적으로 파고 들어가면서 가장 낮은 곳에 cnt 1을 위치시킴
        make_bin_tree(2*start)
        complete_bin_tree[start] = cnt
        cnt += 1
        # 가장 커야 하는 오른쪽 자식 노드
        make_bin_tree(2*start+1)


if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T+1):
        N = int(input())
        
        complete_bin_tree = [0] * (N+1)

        cnt = 1
        make_bin_tree(1)

        print(f"#{tc} {complete_bin_tree[1]} {complete_bin_tree[N//2]}")