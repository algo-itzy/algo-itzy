t = int(input())

for i in range(t):
  ps = input() # ps : 괄호 문자열

  while ps.find('()') != -1: # find() : 특정 문자의 위치 반환. 없으면 -1
    ps = ps.replace('()', '') # replace("찾을값", "바꿀값")

  if ps != '':
    print('NO')
  else:
    print('YES')

"""
아이디어
- 마치 양파처럼 속에 있는 ()부터 하나씩 없애본다.
- find(), replace() 라는 나름 생소한 메서드를 사용하였다.
"""