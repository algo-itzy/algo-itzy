import sys
input = sys.stdin.readline
from collections import defaultdict

# 나이에 따라 요소에 접근하기 위해 default dict를 썼습니다.
N = int(input())
join_li = defaultdict(list)
# 중복된 나이검색을 피하고자 set에 담았다가 list로 변환했습니다.
ages = set()
for _ in range(N):
    age,name = input().split()
    join_li[int(age)] += [name]
    ages.add(int(age))

new_ages = list(ages)
# 나이순서대로 출력하고자 정렬했습니다.
new_ages.sort()

for age in new_ages:
    for name in join_li[age]:
        print(age,name)