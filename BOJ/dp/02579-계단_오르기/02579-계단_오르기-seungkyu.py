'''
점화식 세우는거 생각보다 어려웠다
'''
# n = 1,2,3 일 때 예외처리..
def dp(n):
    if n == 1:
        return (stairs[0])
    elif n == 2:
        return (stairs[0] + stairs[1])
    elif n == 3:
        return (max(stairs[1] + stairs[2], stairs[0] + stairs[2]))
    else:
        ans.append(stairs[0])
        ans.append(stairs[0] + stairs[1])
        ans.append(max(stairs[1] + stairs[2], stairs[0] + stairs[2]))
        for i in range(3, n):
            ans.append(max(ans[i-3] + stairs[i-1] + stairs[i], ans[i-2] + stairs[i]))
        return ans[n-1]

n = int(input())
stairs = []
ans = []
for _ in range(n):
    stairs.append(int(input()))
print(dp(n))
