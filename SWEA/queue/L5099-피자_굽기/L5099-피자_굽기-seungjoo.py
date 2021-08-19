from collections import deque

for test in range(1,int(input())+1):
    N, M = map(int, input().split())
    pizzas = list(map(int,input().split()))
    pizzas_idx = [[pizza,idx+1] for idx, pizza in enumerate(pizzas)]
    oven = deque()
    # 오븐의 크기 N
    for pizza in pizzas_idx:
        oven.append(pizza)
        while len(oven) == N:
            oven.rotate(-1)
            oven[-1][0] //=2
            if not oven[-1][0]:
                oven.pop()
    while len(oven)>1:
        oven.rotate(-1)
        oven[-1][0] //=2
        if not oven[-1][0]:
            oven.pop()
    answer = oven[-1][1]
    print(f'#{test} {answer}')