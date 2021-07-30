n = int(input())
n_list = list(map(int, input().split()))
n_list.sort() # 이진탐색의 선행 조건

m = int(input())
m_list = list(map(int, input().split()))


def binary_search(x):
  start, end = 0, n-1
  
  while start <= end:
    mid = (start+end) // 2
  
    if n_list[mid] < x:
      start = mid+1
    elif n_list[mid] > x:
      end = mid-1
    else:  
      return 1  # 이진탐색 성공

  return 0  # 이진탐색 실패

for x in m_list:
  print(binary_search(x))

# 1. set 단순 비교: 시간 초과
# 2. 교집합 추려낸 후 비교: 시간 초과
# 시간 복잡도를 고려해야 한다. -> 이진탐색
# 변수명 x가 맘에 안듦