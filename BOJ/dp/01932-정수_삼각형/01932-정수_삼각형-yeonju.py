n = int(input())

nums = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(i+1):
        if j == 0: # 양 끝에 있는 요소들은 그냥 바로 위층의 값에다 누적하기
            nums[i][j] += nums[i-1][0]
        elif j == i:
            nums[i][j] += nums[i-1][-1]
        else:
            nums[i][j] += max(nums[i-1][j-1], nums[i-1][j])

print(max(nums[-1]))

# git commit -m "code: Solve boj 01932 정수 삼각형 (yeonju)"