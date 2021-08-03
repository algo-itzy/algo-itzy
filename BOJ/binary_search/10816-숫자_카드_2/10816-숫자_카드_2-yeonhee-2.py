# 모듈 없이 풀기

import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
M = int(input())
key_nums = list(map(int, input().split()))

# dict comprehension을 이용해 key는 key_nums, value는 0으로 초기화
result = {key: 0 for key in key_nums}

for number in numbers:
    if number in result.keys():
        result[number] += 1

for key_num in key_nums:
    print(result[key_num], end = ' ')

"""
마지막 for문에서 딕셔너리 순서를 이용해서 출력하면
답이 틀렸다고 나옵니다.

(예시)

for v in result.values():
    print(v, end = ' ')

이유는 잘 모르겠습니다.

혹시나 해서 collections.OrderedDict로 풀어봤는데도 틀렸다고 하네요.
"""