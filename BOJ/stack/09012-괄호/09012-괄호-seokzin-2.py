def is_vps(ps):
  stack = [] # 괄호 담을 스택

  for p in ps:
    if p == '(':
      stack.append('(')
    else: # p == ')'
      if stack: # 스택이 안 비었다면
        stack.pop()
      else: 
        return 'NO'

  if stack: # 마지막에 스택이 안 비었다면
    return 'NO'
  else:
    return 'YES'

t = int(input())

for _ in range(t):
  ps = input() # ps : 괄호 문자열

  print(is_vps(ps))


"""

아이디어 : 문제 의도에 맞게 일부러 스택을 써봤다.
1. '('을 만나면 스택에 '('을 담는다. 
2. ')'을 만나면 스택에 '('을 뺀다.
3. 만일 스택이 비었는데 ')'을 만나면 이는 VPS가 아니다.
4. 또한 for문이 끝나고 스택이 안 비었다면 이는 VPS가 아니다.

"""