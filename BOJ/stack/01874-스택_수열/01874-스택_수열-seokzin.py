def is_seq(s):
  now = 1

  for num in nums:
    while now <= num:
      stack.append(now)
      now += 1
      op.append('+')

    if stack[-1] == num:
      stack.pop()
      op.append('-')
    else:
      return False

  return True

n = int(input())
stack = []
nums = []  # 정수 리스트
op = []  # NO case 때문에 연산자는 리스트에 담아뒀다 마지막에 출력해야함

for _ in range(n):
  nums.append(int(input()))

if is_seq(nums):
  print(*op, sep='\n')
else:
  print('NO')

"""
처음엔 일일이 push, pop 하지 않고 리스트만 가지고 판별하는 문제인줄 앎
근데 단순하게 해도 맞는 것을 보니 티어에 맞는 난이도라 생각
"""