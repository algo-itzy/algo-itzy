# git commit -m "code: Solve programmers 표 편집 (jiwoong)"
from collections import deque


def solution(n, k, cmd):
    arr = deque([i for i in range(n)])
    tmp = deque()

    for i in cmd:
        s_arr = i.split()

        if len(s_arr) > 1:
            word, x = s_arr[0], int(s_arr[1])
            if word == "D":
                k += x
            elif word == "U":
                k -= x
        else:
            word = s_arr[0]
            if word == "C":
                tmp.append((k, arr[k]))
                arr.remove(arr[k])
                if k == len(arr):
                    k -= 1
            elif word == "Z":
                ok, ox = tmp.pop()
                if ok <= k:
                    k += 1
                arr.insert(ok, ox)

    words = set(arr)
    result = ""

    for i in range(n):
        if i in words:
            result += 'O'
        else:
            result += 'X'
    return result
