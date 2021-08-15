from heapq import heappop,heappush
from math import ceil

def find_time_units(n):

    students = []
    for _ in range(n):
        start, end = map(int,input().split())
        if start > end:
            start, end = end, start
        start = ceil(start/2)
        end = ceil(end/2)
        students.append([start,end])
    students.sort()
    
    time_units = []
    heappush(time_units,students[0][1])

    for i in range(1,n):
        if time_units[0] >= students[i][0]:
            heappush(time_units,students[i][1])
        else:
            heappop(time_units)
            heappush(time_units,students[i][1])

    return len(time_units)

for test in range(1,int(input())+1):
    N = int(input())
    print(f'#{test} {find_time_units(N)}')