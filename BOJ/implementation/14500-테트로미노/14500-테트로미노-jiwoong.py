# git commit -m "code: Solve boj 14500 테트로미노 (jiwoong)"
n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
total_max = 0

# 정사각형
for i in range(n - 1):
    for j in range(m - 1):
        temp = paper[i][j] + paper[i + 1][j] + paper[i][j + 1] + paper[i + 1][j + 1]
        if total_max < temp:
            total_max = temp

# 일자 긴거 가로
for i in range(n):
    for j in range(m - 3):
        temp = paper[i][j] + paper[i][j + 1] + paper[i][j + 2] + paper[i][j + 3]
        if total_max < temp:
            total_max = temp

# 일자 긴거 세로
for i in range(n - 3):
    for j in range(m):
        temp = paper[i][j] + paper[i + 1][j] + paper[i + 2][j] + paper[i + 3][j]
        if total_max < temp:
            total_max = temp

# L자 
for i in range(n - 2):
    for j in range(m - 1):
        temp = paper[i][j] + paper[i + 1][j] + paper[i + 2][j] + paper[i + 2][j + 1]
        if total_max < temp:
            total_max = temp

# L자 대칭
for i in range(n - 2):
    for j in range(1, m):
        temp = paper[i][j] + paper[i + 1][j] + paper[i + 2][j] + paper[i + 2][j - 1]
        if total_max < temp:
            total_max = temp

# ㄱ자
for i in range(n - 1):
    for j in range(m - 2):
        temp = paper[i][j] + paper[i][j + 1] + paper[i][j + 2] + paper[i + 1][j + 2]
        if total_max < temp:
            total_max = temp

# ㄱ자 대칭
for i in range(n - 1):
    for j in range(m - 2):
        temp = paper[i][j] + paper[i + 1][j] + paper[i][j + 1] + paper[i][j + 2]
        if total_max < temp:
            total_max = temp

# # ㄱ자 위에 짧은거
for i in range(n - 2):
    for j in range(m - 1):
        temp = paper[i][j] + paper[i][j + 1] + paper[i + 1][j + 1] + paper[i + 2][j + 1]
        if total_max < temp:
            total_max = temp

# ㄱ자 위에 짧은거 대칭
for i in range(n - 2):
    for j in range(m - 1):
        temp = paper[i][j] + paper[i][j + 1] + paper[i + 1][j] + paper[i + 2][j]
        if total_max < temp:
            total_max = temp

# ㄴ자
for i in range(n - 1):
    for j in range(m - 2):
        temp = paper[i][j] + paper[i + 1][j] + paper[i + 1][j + 1] + paper[i + 1][j + 2]
        if total_max < temp:
            total_max = temp

# ㄴ자 대칭
for i in range(1, n):
    for j in range(m - 2):
        temp = paper[i][j] + paper[i][j + 1] + paper[i][j + 2] + paper[i - 1][j + 2]
        if total_max < temp:
            total_max = temp
# ㅜ자
for i in range(n - 1):
    for j in range(m - 2):
        temp = paper[i][j] + paper[i][j + 1] + paper[i + 1][j + 1] + paper[i][j + 2]
        if total_max < temp:
            total_max = temp

# ㅗ자
for i in range(1, n):
    for j in range(m - 2):
        temp = paper[i][j] + paper[i][j + 1] + paper[i - 1][j + 1] + paper[i][j + 2]
        if total_max < temp:
            total_max = temp

# ㅓ자. 다시 확인?
for i in range(1, n - 1):
    for j in range(m - 1):
        temp = paper[i][j] + paper[i][j + 1] + paper[i - 1][j + 1] + paper[i + 1][j + 1]
        if total_max < temp:
            total_max = temp
# print(total_max)

# ㅏ자
for i in range(n - 2):
    for j in range(m - 1):
        temp = paper[i][j] + paper[i + 1][j] + paper[i + 2][j] + paper[i + 1][j + 1]
        if total_max < temp:
            total_max = temp

# 이상한 모양
for i in range(n - 2):
    for j in range(m - 1):
        temp = paper[i][j] + paper[i + 1][j] + paper[i + 1][j + 1] + paper[i + 2][j + 1]
        if total_max < temp:
            total_max = temp

# 이상한 모양 90도 회전
for i in range(1, n):
    for j in range(m - 2):
        temp = paper[i][j] + paper[i][j + 1] + paper[i - 1][j + 1] + paper[i - 1][j + 2]
        if total_max < temp:
            total_max = temp

# 이상한 모양 반전
for i in range(n - 2):
    for j in range(1, m):
        temp = paper[i][j] + paper[i + 1][j] + paper[i + 1][j - 1] + paper[i + 2][j - 1]
        if total_max < temp:
            total_max = temp

# 이상한 모양 90도 회전의 반전
for i in range(n - 1):
    for j in range(m - 2):
        temp = paper[i][j] + paper[i][j + 1] + paper[i + 1][j + 1] + paper[i + 1][j + 2]
        if total_max < temp:
            total_max = temp

print(total_max)
