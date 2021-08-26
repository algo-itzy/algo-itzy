import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):

    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))  # 치즈 양
    pizza = list(i for i in range(M))  # 피자 인덱스 0부터 시작, 추후 보정
    queue = deque(i for i in range(N))  # 오븐

    # 오븐에 피자가 1개 남을 때까지 계속 진행
    while len(queue) > 1:

        if cheese[queue[0]]:  # 치즈 남아있을 때
            cheese[queue[0]] //= 2
            queue.append(queue.popleft())  # 한 칸 rotate
        else:  # 치즈 다 녹았을 때
            queue.popleft()
            if N != M:  # 오븐에 들어갈 피자 남아있을 때
                queue.appendleft(pizza[N])
                N += 1

    print(f'#{test_case} {queue.pop()+1}')
