import sys
from math import factorial

N = int(input())
res = str(factorial(N))  # 뒤에서부터 체크하기위해 str로 변환
cnt = 0
for i in range(len(res)):
    if res[-1-i] == '0':
        cnt += 1
    else:
        print(cnt)
        break


# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return factorial(n-1)*n
# 메모리 초과..