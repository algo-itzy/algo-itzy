import sys
input = sys.stdin.readline

n = int(input())
stack = []

for i in range(n):
  cmd = input().split() # input을 가변 길이 '리스트'로 받음

  if cmd[0] == 'push':
    stack.append(cmd[1])
  elif cmd[0] == 'pop':
    print(stack.pop() if stack else -1)
  elif cmd[0] == 'size':
    print(len(stack))
  elif cmd[0] == 'empty':
    print(1 if not stack else 0)
  else: # cmd[0] == 'top'
    print(stack[-1] if stack else -1)

"""

1. One-liner if statement 사용하여 코드 간결화

2. 시간 복잡도 고려한 설계
  pop(), append() = O(1)
  remove(), insert() = O(N)

3. input이 10000개 정도 되니 import sys가 필요하다.

"""