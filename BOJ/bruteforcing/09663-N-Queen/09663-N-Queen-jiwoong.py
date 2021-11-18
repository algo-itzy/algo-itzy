# git commit -m "code: Solve boj 09663 N-Queen (jiwoong)"
def n_queen(row, diagonal, reversal, visited):
    global ans

    if row < N + 1:
        for col in range(N):
            if row + col not in diagonal:
                if col - row not in reversal:
                    if col not in visited:  
                        diagonal.append(row + col)
                        reversal.append(col - row)
                        visited.append(col)
                        n_queen(row + 1, diagonal, reversal, visited)
                        diagonal.pop()
                        reversal.pop()
                        visited.pop()
        # 끝까지
        if row == N:
            ans += 1


N = int(input())
ans = 0
for i in range(N):
    n_queen(1, [i], [i], [i])
print(ans)
