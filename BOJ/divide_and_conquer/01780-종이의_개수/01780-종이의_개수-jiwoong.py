import sys


def check(s_x, s_y, length):  # 시작 x, y좌표, 종이 길이
    global ans
    arr = []  # 숫자값을 넣을 리스트
    for i in range(s_x, s_x + length):
        for j in range(s_y, s_y + length):
            if matrix[i][j] not in arr:  # 없으면 추가
                arr.append(matrix[i][j])
            if len(arr) >= 2:  # 두개 이상이면 divide
                divide(s_x, s_y, length)
                return
    # 같은 종이로 이루어진 경우 : N % 3 = 0
    if arr[0] == -1:
        ans[0] += 1
    elif arr[0] == 0:
        ans[1] += 1
    elif arr[0] == 1:
        ans[2] += 1


# 9칸 divide
def divide(s_x, s_y, length):
    global ans
    if length == 1:
        ans[matrix[s_x][s_y]] += 1
        return  # stop
    k = length // 3
    check(s_x, s_y, k)
    check(s_x, s_y + k, k)
    check(s_x, s_y + 2 * k, k)
    check(s_x + k, s_y, k)
    check(s_x + k, s_y + k, k)
    check(s_x + k, s_y + 2 * k, k)
    check(s_x + 2 * k, s_y, k)
    check(s_x + 2 * k, s_y + k, k)
    check(s_x + 2 * k, s_y + 2 * k, k)


input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
ans = [0, 0, 0]  # -1개수, 0개수, 1개수
check(0, 0, N)

print(ans[0])
print(ans[1])
print(ans[2])
