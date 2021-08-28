def method(num):
    global ans
    if num > N:
        return
    elif num == N:
        ans += 1
    else:
        method(num + 1)
        method(num + 2)
        method(num + 3)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    ans = 0
    method(0)

    print(ans)
