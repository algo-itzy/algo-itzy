N = int(input())
N_list = list(map(int, input().split()))
N_list.sort()

M = int(input())
M_list = list(map(int, input().split()))

dic = {}

for n in N_list:
  if n in dic:
    dic[n] += 1
  else:
    dic[n] = 1

for m in M_list:
  print(dic[m] if m in dic else 0, end=' ')

# 딕셔너리가 효율이 생각보다 좋았다.
# 이런 문제는 변수명이 고민이 된다.
# print한줄 조건문과 end 연계는 처음 해봤다. 되네요!

"""
git commit -m "code: Solve boj 10816 숫자 카드 2 (seokzin)"
"""