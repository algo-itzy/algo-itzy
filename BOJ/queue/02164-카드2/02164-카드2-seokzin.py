from collections import deque

n = int(input())

deq = deque(i for i in range(1, n+1))

for _ in range(n-1):
  deq.popleft()
  deq.append(deq.popleft())

print(deq[0])

# 어차피 n-1번 반복하기 때문에 while len(deq) > 1 보다 for(n-1)이 성능 좋다
