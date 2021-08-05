N, M = map(int, input().split()) # 카드의 개수 N, M

arr = list(map(int, input().split())) # 카드에 적혀있는 수를 list 에 저장

result = 0

for i in range(N): # 3개의 카드를 살펴볼 모든 경우의 수 - 3중 for 문
   for j in range(i+1, N):
       for k in range(j+1, N):
           if arr[i] + arr[j] + arr[k] > M:
               continue
           else:
               result = max(result, arr[i]+arr[j]+arr[k]) # 그 중 최댓값을 result 로 출력
print(result)
  

"""
git commit -m "code: Solve boj 00000 문제 이름 (yeonju)"
"""