t = int(input())

for _ in range(t):
  h, w, n = map(int, input().split())
  room = (((n-1)%h)+1)*100 + (((n-1)//h)+1)
  
  print(room)

# 예외 처리를 없애고 싶어서 n-1을 활용했습니다

"""
git commit -m "code: Solve boj 10250 ACM 호텔 (seokzin)"
"""