# 시간 초과입니다. 더 효율적인 풀이가 생각이 안나네요 ㅠㅜ

import sys
input = sys.stdin.readline

N = int(input())  # 이동할 채널
M = int(input())  # 고장난 버튼의 갯수
btn = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
if M != 0:
    off = list(map(int, input().split()))
    for i in off:
        btn.remove(i)

num1, num2 = N, N
ans = []

if N > 100:
    off = N - 100
    ans.append(off)
else:
    on = 100 - N
    ans.append(on)

while True:  # +
    num1 += 1
    flag = 0
    for i in str(num1):
        if int(i) not in btn:  # 안될 떄
            flag = 1
    if flag == 0:  # 될 때
        ans.append(len(str(num1)) + num1 - N)
        break

while True:  # -
    num2 -= 1
    flag = 0
    for i in str(num2):
        if int(i) not in btn:  # 안될 때
            flag = 1
    if flag == 0:  # 될 때
        ans.append(len(str(num1)) + num1 - N)
        break
    if num2 == 0:
        break

if M == 0:
    ans.append(len(str(N)))

print(min(ans))
