def solution(m, n, board):
    answer = 0
    graph = list(map(list, zip(*board)))

    def pop_block():
        popped_set = set()

        for r in range(n-1):
            for c in range(m-1):
                if graph[r][c] == graph[r+1][c] == graph[r][c+1] == graph[r+1][c+1] != 0:
                    popped_set.update({(r, c), (r+1, c), (r, c+1), (r+1, c+1)})

        for r, c in popped_set:
            graph[r][c] = 0

        for idx, row in enumerate(graph):
            tmp = [0]*row.count(0) + [block for block in row if block != 0]
            graph[idx] = tmp

        return len(popped_set)

    while 1:
        cnt = pop_block()
        if not cnt:
            return answer
        answer += cnt


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
