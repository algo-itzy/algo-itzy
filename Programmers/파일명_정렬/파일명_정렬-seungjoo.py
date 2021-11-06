# git commit -m "code: Solve programmers 파일명 정렬 (seungjoo)"
from heapq import heappop, heappush

def solution(files):
    answer = []
    sort_arr = []
    for pos, each_file in enumerate(files):
        tmp = each_file + 'f'
        flag = 0
        for idx, char in enumerate(tmp):
            if not flag and char.isdigit():
                start = idx
                flag = 1
            elif flag and not char.isdigit():
                end = idx
                break
        head, number = each_file[:start], each_file[start:end]
        heappush(sort_arr, (head.lower(), int(number), pos))
    while sort_arr:
        h, n, p = heappop(sort_arr)
        answer.append(files[p])
    return answer