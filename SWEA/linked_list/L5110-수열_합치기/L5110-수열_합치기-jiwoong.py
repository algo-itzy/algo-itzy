def mergeSeq():
    first_seq = list(map(int, input().split()))
    for _ in range(M - 1):
        newSeq = list(map(int, input().split()))
        seq_len = len(first_seq)
        for i in range(len(first_seq)):
            if first_seq[i] > newSeq[0]:
                first_seq[i:0] = newSeq
                break
        if len(first_seq) == seq_len:
            first_seq += newSeq
    return first_seq


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    ans = mergeSeq()
    print(f'#{tc}', end=' ')
    print(' '.join(str(n) for n in ans[-1:-11:-1]))