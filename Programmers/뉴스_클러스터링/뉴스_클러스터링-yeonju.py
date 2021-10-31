from itertools import chain
from collections import defaultdict


def solution(str1, str2):

    dict1 = {}                          # str1 의 집합을 담을 리스트 생성
    dict2 = {}                          # str2 "
    sum_of_sets = 0
    intersection = 0

    for i in range(0, len(str1)-1):     # str1 문자열 2개 묶음씩 가져와서 조건에 만족하는 원소들 추가
        x, y = str1[i], str1[i+1]
        addition = x+y
        if addition.isalpha():
            addition = addition.lower()
            if addition in dict1:       # 딕셔너리를 이용해 동일한 원소에 해당되는 개수만 value 에 더해줌
                dict1[addition] += 1
            else:
                dict1[addition] = 1

    for i in range(0, len(str2)-1):
        x, y = str2[i], str2[i+1]
        addition = x+y
        if addition.isalpha():
            addition = addition.lower()

            if addition in dict2:
                dict2[addition] += 1
            else:
                dict2[addition] = 1

    dict3 = defaultdict(list)       # dict1과 dict2를 합쳐줄 새로운 딕셔너리 생성

    for k, v in chain(dict1.items(), dict2.items()):
        dict3[k].append(v)

    for k, v in dict3.items():      # 합집합 개수는 해당 원소의 value 값들 중 큰 것을 택하면 됨
        sum_of_sets += max(v)

        if len(v) > 1:              # 집합 개수는 해당 원소의 value 값들 중 더 작은 것을 택하면 됨
            intersection += min(v)  # 만약에 하나의 딕셔너리에만 원소가 들어있었다면, 그 원소는 교집합에 해당되기 않기에 무시함

    if intersection == 0 and sum_of_sets == 0: # 두 집합이 모두 공집합인 경우
        return 65536
    else:
        return ((intersection / sum_of_sets) * 65536) // 1


# print(solution('aa1+aa2', 'AAAA12'))
print(solution('E=M*C^2', 'e=m*c^2'))

# git commit -m "code: Solve programmers 뉴스 클러스터링 (yeonju)"