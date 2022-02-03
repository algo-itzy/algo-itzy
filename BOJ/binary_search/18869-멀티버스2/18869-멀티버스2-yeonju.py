m, n = map(int, input().split())

li = [list(enumerate(map(int, input().split()))) for _ in range(m)]

dic = {}
ans = 0
for j in range(m):
    ordered = sorted(li[j], key=lambda x: x[1])
    new = ''
    # print('ddd',ordered)

    for i in range(0, len(ordered)-1):
        new += str(ordered[i][0])
        if ordered[i+1][1] and ordered[i][1] == ordered[i+1][1]:
                new += '.'
    new += str(ordered[-1][0])
    # print(new)

    if new in dic:
        dic[new] += 1
    else:
        dic[new] = 1

# print(dic)
for value in dic.values():
    ans += value * (value - 1) // 2


print(ans)


# git commit -m "code: Solve boj 18869 멀티버스2 (yeonju)"