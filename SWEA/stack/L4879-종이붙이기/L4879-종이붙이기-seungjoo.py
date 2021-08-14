import sys
input = sys.stdin.readline

def stick_paper(n):
    length = n//10
    dp = [0] * (length+1)
    dp[0],dp[1] = 1,1
    for i in range(2,length+1):
        dp[i] = dp[i-2]*2 + dp[i-1]
    return dp[length]


for test in range(1,int(input())+1):
    print(f'#{test} {stick_paper(int(input()))}')


# sys.setrecursionlimit(10**6)

# # DFS 했씀니다 안댑니다.
# def stick_paper(n):
#     global cnt
#     if not n:
#         cnt += 1
#         return
#     for block in 'abc':
#         if n >= size[block]:
#             stick_paper(n-size[block])


# for test in range(1,int(input())+1):
#     cnt = 0
#     size = {'a':10, 'b':20, 'c':20}
#     stick_paper(int(input()))
#     print(f'#{test} {cnt}')