# git commit -m "code: Solve programmers 표 편집 (seungjoo)"
from heapq import heappop, heappush

def solution(n, k, cmd):
    left, right, delete = [-i for i in range(k-1, -1, -1)], [i for i in range(k, n)], []
    for command in cmd:
        c, *num = command.split()
        if c == 'U':
            cnt = int(num.pop())
            for _ in range(cnt):
                heappush(right, -heappop(left))
        elif c == 'D':
            cnt = int(num.pop())
            for _ in range(cnt):
                heappush(left, -heappop(right))
        elif c == 'C':
            delete.append(heappop(right))
            if not right:
                heappush(right, -heappop(left))
        else:
            now = delete.pop()
            if now > right[0]:
                heappush(right, now)
            else:
                heappush(left, -now)
    answer, idx = '', 0
    while left:
        heappush(right, -heappop(left))
    while right:
        now = heappop(right)
        while idx != now:
            idx += 1
            answer += 'X'
        answer += 'O'
        idx += 1
    while idx != n:
        answer += 'X'
        idx += 1
    return answer
            