from collections import Counter


def solution(str1, str2):
    answer = 0

    a = []
    b = []

    for i in range(len(str1)-1):
        tmp = str1[i:i+2]

        if tmp.isalpha():
            a.append(str1[i:i+2].lower())

    for i in range(len(str2)-1):
        tmp = str2[i:i+2]

        if tmp.isalpha():
            b.append(str2[i:i+2].lower())

    ca = Counter(a)
    cb = Counter(b)

    inter = sum((ca & cb).values())
    union = sum((ca | cb).values())

    answer = inter/union if union else 1

    return int(answer * 65536)

# Counter에도 set 메서드 사용이 가능! - 신기하게 동작