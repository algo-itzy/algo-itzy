# 오븐 갯수만 빼면 원형 테이블에서 사람 죽이는 문제랑 같은듯
from collections import deque


inputs = lambda : map(int, input().split())


def bake(Pizzas):
    # cold oven
    oven = deque()
    for _ in range(N):
        oven.append(Pizzas.popleft())

    # heated oven
    while oven:
        pizza = oven.popleft()
        pizza[1] //= 2
        if pizza[1]:
            oven.append(pizza)
        elif Pizzas:
            oven.append(Pizzas.popleft())
        if len(oven) == 1:
            return oven.popleft()[0]


if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T+1):
        N, M = inputs()

        Pizzas = inputs()
        Pizzas = deque([[i+1, v] for i, v in enumerate(Pizzas)])

        last = bake(Pizzas)
        
        print(f"#{tc} {last}")