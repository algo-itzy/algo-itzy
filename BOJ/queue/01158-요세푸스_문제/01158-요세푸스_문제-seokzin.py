n, k = map(int, input().split())

arr_a = [i for i in range(1,n+1)]
arr_k = [] # 사망자
idx = 0

while arr_a:
  idx = (idx + (k-1)) % len(arr_a)
  arr_k.append(arr_a.pop(idx))

print(f"<{', '.join(map(str, arr_k))}>")

# 출력부가 까다로운 문제
# join() - 리스트 사이에 기호를 넣어 문자열로 표현. 다만 join의 변수는 str
# 또는 *arr_k, sep=", " 를 활용할 수도 있다