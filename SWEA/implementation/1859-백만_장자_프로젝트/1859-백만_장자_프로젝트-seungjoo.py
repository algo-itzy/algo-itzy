

for test in range(1,int(input())+1):
    N = int(input())
    prices = list(map(int, input().split()))
    answer = 0
    max_price = 0 
    for j in range(N-1,-1,-1):
        if max_price > prices[j]:
            answer += max_price - prices[j]
        else:
            max_price = prices[j]

    print(f'#{test} {answer}')