arr = input().split('-')  # - 기준으로 괄호 묶으면 최소다
res = sum(map(int, arr.pop(0).split('+')))  # 첫 덩어리는 양수로 넣자

for x in arr:
    temp = x.split('+')
    res -= sum(map(int, temp))

print(res)
