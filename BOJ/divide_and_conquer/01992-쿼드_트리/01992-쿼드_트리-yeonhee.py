import sys
input = sys.stdin.readline


def quad_tree(r, c, n):
    tmp = video[r][c]

    for i in range(r, r+n):
        for j in range(c, c+n):
            if tmp != video[i][j]:
                result.append("(")
                quad_tree(r, c, n//2)
                quad_tree(r, c + n//2, n//2)
                quad_tree(r + n//2, c, n//2)
                quad_tree(r + n//2, c + n//2, n//2)
                result.append(")")
                return
    result.append(tmp)


n = int(input())

video = [list(map(int, input().strip())) for _ in range(n)]
result = []

quad_tree(0, 0, n)
print(''.join(map(str, result)))
