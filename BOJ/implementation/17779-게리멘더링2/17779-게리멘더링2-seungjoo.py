# git commit -m "code: Solve boj 17779 게리멘더링2 (seungjoo)"
import sys
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
answer = float('inf')
total = 0
for i in range(N):
    for j in range(N):
        total += matrix[i][j]
for x in range(N - 1):
    for y in range(1, N - 1):
        for d1 in range(1, min(y + 1, N - x - 1)):
            for d2 in range(1, min(N - y, N - x - d1)):
                area1 = 0
                for i in range(x):
                    for j in range(y + 1):
                        area1 += matrix[i][j]
                for i in range(x, x + d1):
                    for j in range(y - d1):
                        area1 += matrix[i][j]
                for i in range(x, x + d1):
                    for j in range(y - d1, y - i + x):
                        area1 += matrix[i][j]
                area2 = 0
                for i in range(x):
                    for j in range(y + 1, N):
                        area2 += matrix[i][j]
                for i in range(x, x + d2 + 1):
                    for j in range(y + d2 + 1, N):
                        area2 += matrix[i][j]
                for i in range(x, x + d2):
                    for j in range(y + i - x + 1, y + d2 + 1):
                        area2 += matrix[i][j]
                        
                area3 = 0
                for i in range(x + d1, N):
                    for j in range(y - d1):
                        area3 += matrix[i][j]
                for i in range(x + d1 + d2 + 1, N):
                    for j in range(y - d1, y - d1 + d2):
                        area3 += matrix[i][j]
                for i in range(x + d1 + 1, x + d1 + d2 + 1):
                    for j in range(y - d1, y - 2 * d1 + i - x):
                        area3 += matrix[i][j]
                area4 = 0
                for i in range(x + d1 + d2 + 1, N):
                    for j in range(y - d1 + d2, N):
                        area4 += matrix[i][j]
                for i in range(x + d2 + 1, x + d1 +d2 + 1):
                    for j in range(y + d2 + 1, N):
                        area4 += matrix[i][j]
                for i in range(x + d2 + 1, x + d1 + d2 + 1):
                    for j in range(y - i + x + 2 * d2 + 1, y + d2 + 1):
                        area4 += matrix[i][j]

                area5 = total - (area1 + area2 + area3 + area4)
                answer = min(answer, max(area1, area2, area3, area4, area5) - min(area1, area2, area3, area4, area5))
print(answer)
