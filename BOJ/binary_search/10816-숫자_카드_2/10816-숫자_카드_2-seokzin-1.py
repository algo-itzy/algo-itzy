def binary_left(x):
  start = 0
  end = n-1

  while start <= end:
    mid = (start+end) // 2

    if n_list[mid] >= x:
      end = mid-1
    elif n_list[mid] < x:
      start = mid+1

  return start


def binary_right(x):
  start = 0
  end = n-1

  while start <= end:
    mid = (start+end) // 2

    if n_list[mid] > x:
      end = mid-1
    elif n_list[mid] <= x:
      start = mid+1

  return end

n = int(input())
n_list = list(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))

n_list.sort()

for x in m_list:
  print(binary_right(x)-binary_left(x)+1, end=' ')

# 시도 1. count - 당연히 시간 초과. - 
# 시도 2. bisect 라이브러리 사용 - 라이브러리에 의존이 좋은 방법은 아닌듯..
# 시도 3. bs_left, bs_right 구현
# 추후 조금 더 리팩토링 해보기
# PyPy3로만 맞는 맘에 안드는 문제

"""
git commit -m "code: Solve boj 10816 숫자 카드 2 (seokzin)"
"""