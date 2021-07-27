import sys
input = sys.stdin.readline

n = int(input())
queue = []

for i in range(n):
  cmd = input().split() 

  if cmd[0] == 'push':
    queue.append(cmd[1])
  elif cmd[0] == 'pop':
    print(queue.pop(0) if queue else -1)
  elif cmd[0] == 'size':
    print(len(queue))
  elif cmd[0] == 'empty':
    print(1 if not queue else 0)
  elif cmd[0] == 'front':
    print(queue[0] if queue else -1)
  else:  # 'back'
    print(queue[-1] if queue else -1)

# 스택 문제의 복붙 수준.. PASS