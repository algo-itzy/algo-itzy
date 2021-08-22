from collections import deque

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    pizza = deque(zip(map(int, input().split()), range(1, m+1)))
    q = deque()

    for i in range(n):  # 처음에 피자 넣기
        q.append(pizza.popleft())

    while len(q) > 1:
        now = q[0] 

        if now[0] > 1:  # 녹일 치즈가 남았을 때
            q.append((now[0]//2, now[1]))
            q.popleft()
        elif now[0] == 1 and pizza:  # 다 녹았고 새 피자 넣을 때
            q.popleft()
            q.appendleft(pizza.popleft())
        elif now[0] == 1 and not pizza:  # 다 녹았고 새 피자 없을 때
            q.popleft()

    print(f'#{tc}', q[0][1])

# appendleft, popleft가 자주 쓰여서 deque이 필수였던 문제