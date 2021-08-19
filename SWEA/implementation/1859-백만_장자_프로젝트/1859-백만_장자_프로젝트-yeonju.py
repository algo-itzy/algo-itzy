t = int(input())

for tc in range(t):
    n = int(input())
    price = list(map(int, input().split()))

    cnt = 0
    maximum = price[-1]             # 맨 뒤의 값을 최댓값으로  설정
    for i in range(n-1, -1, -1):    # 뒤에서부터 앞으로 확인해오기
        if price[i] > maximum:      # 최댓값 갱신
            maximum = price[i]
        else:
            cnt += maximum - price[i] # 차익 계산 

    print(f'#{tc+1} {cnt}')



# 아래 풀이는 통과가 안 되네요,, 메모리를 많이 차지해서 그런지 ㅇ_0
# t = int(input())
#
# for tc in range(t):
#
#     n = int(input())
#
#     price = list(map(int, input().split()))
#     order_price = sorted(price, reverse = True)
#     # print(order_price)
#
#     profit = 0
#
#     for i in range(0,n):
#         for j in range(0,n):
#             if price[i] < order_price[j] and price.index(order_price[j]) > i:
#                 profit += order_price[j] - price[i]
#                 break
#
#     print(f'#{tc+1} {profit}')
#