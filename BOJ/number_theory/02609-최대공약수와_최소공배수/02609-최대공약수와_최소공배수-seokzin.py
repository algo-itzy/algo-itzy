a, b = map(int, input().split())

def gcd(x, y):
  if y == 0:
    return x
  return gcd(y, x%y)

gcd = gcd(a, b)
lcm = a*b // gcd

print(gcd)
print(lcm)

# 일부러 재귀를 사용
# gcd() 연산을 2번 하기 싫어 lcm 함수 선언 X

"""
git commit -m "code: Solve boj 00000 문제 이름 (seokzin)"
"""