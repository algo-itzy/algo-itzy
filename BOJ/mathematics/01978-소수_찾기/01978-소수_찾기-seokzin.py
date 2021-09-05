n = int(input())
nums = list(map(int,input().split()))
prime = 0 # 소수 개수

for num in nums:
  if num == 1:
    continue

  elif num == 2:
    prime += 1
    continue

  else:  # num > 2
    for x in range(2, num):
      if num % x == 0:
        break
    else:
      prime += 1  # for문 무사 통과시 -> 소수다
  
print(prime)

# for-else 문을 써보고싶었음
# 근데 for-else 쓸 상황이면 대부분 함수가 더 좋다