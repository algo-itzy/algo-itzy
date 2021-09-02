# - 를 기준으로 다음 - 가 나오기 전까지 다 더하기

expression = input().split('-')

num = []

for i in expression:
    cnt = 0
    expression2 =i.split('+')

    for j in expression2:
        cnt += int(j)
    num.append(cnt)

n = num[0]
for i in range(1,len(num)):
    n -= num[i]

print(n)

# git commit -m "code: Solve boj 01541 잃어버린 괄호 (yeonju)"