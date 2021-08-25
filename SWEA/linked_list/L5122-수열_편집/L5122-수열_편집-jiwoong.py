T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    seq = input().split()

    for _ in range(M):
        op = input().split()
        # 추가, 뒤로 이동
        if op[0] == 'I':
            seq.insert(int(op[1]), op[2])
        # 삭제, 앞으로 이동
        elif op[0] == 'D':
            seq.pop(int(op[1]))
        # 변경
        else:
            seq[int(op[1])] = op[2]
    # 존재 안하면
    ans = -1

    if len(seq) > L:
        ans = seq[L]

    print('#{} {}'.format(tc, ans))
