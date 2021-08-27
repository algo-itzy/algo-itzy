import sys

input = sys.stdin.readline

s = set()
s_all = set(map(str, range(1, 21))) # 최초 선언후 재사용이 효율적

for _ in range(int(input())):
  cmd = input().split()

  if cmd[0] == 'add':
    s.add(cmd[1])
  elif cmd[0] == 'remove':
    s.discard(cmd[1])
  elif cmd[0] == 'check':
    print(1 if cmd[1] in s else 0)
  elif cmd[0] == 'toggle':
    s.discard(cmd[1]) if cmd[1] in s else s.add(cmd[1])
  elif cmd[0] == 'all':
    s = s_all
  elif cmd[0] == 'empty':
    s = set()


# set remove는 요소 없으면 에러. discard는 요소 없어도 작동

'''
# i for i in range(20) VS range(20)

바로 넣어줄땐 range가 빠르지만 미리 선언을 하고 대입을 할땐 generator 가 빠르다.

https://www.acmicpc.net/board/view/57656

'''