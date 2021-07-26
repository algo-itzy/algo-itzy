from sys import stdin
input = stdin.readline

s1 = list(input().strip())
s2 = list()

n = int(input())

for _ in range(n):
  cmd = input().split()

  if cmd[0] == 'L' and s1:
    s2.append(s1.pop())

  elif cmd[0] == 'D' and s2:
    s1.append(s2.pop())

  elif cmd[0] == 'B' and s1:
    s1.pop()

  elif cmd[0] == 'P':
    s1.append(cmd[1])

print(''.join(s1+s2[::-1]))

"""
- input()에 자꾸 개행 발생 -> strip() 추가
- insert 성능 비교
  1. 문자열 직접 자르기 -> 가장 빠름
  2. list 직접 슬라이싱
  3. insert()
- 하지만 insert, remove 자체가 O(n)이기 때문에 pop, append로 대체해야 한다.
- 그래서 스택 2개를 활용한다. -> 발상이 천재적이다.. 이게 왜 실3
- 스택 2개가 커서 위치까지 대체한다..
"""