# git commit -m "code: Solve programmers 뉴스 클러스터링 (jiwoong)"
from collections import Counter


def solution(str1, str2):
    str1 = str1.lower()  # 모두 소문자로
    str2 = str2.lower()

    arr1 = []
    arr2 = []
    for i in range(len(str1) - 1):
        if str1[i:i + 2].isalpha():  # 2개씩 끊고 문자열만
            arr1.append(str1[i:i + 2])

    for i in range(len(str2) - 1):
        if str2[i:i + 2].isalpha():
            arr2.append(str2[i:i + 2])

    c1 = Counter(arr1)
    c2 = Counter(arr2)

    min_arr = [min(c1[i], c2[i]) * [i] for i in list(set(c1) & set(c2))]
    max_arr = [max(c1[i], c2[i]) * [i] for i in list(set(c1) | set(c2))]

    a1 = 0
    for i in range(len(min_arr)):
        for j in range(len(min_arr[i])):
            a1 += 1
    a2 = 0
    for i in range(len(max_arr)):
        for j in range(len(max_arr[i])):
            a2 += 1
    if a1 == 0 and a2 == 0:
        return 65536
    else:
        return int(a1 / a2 * 65536)
