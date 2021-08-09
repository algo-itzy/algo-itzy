import sys
input = sys.stdin.readline

time_list = [list(map(int, input().split())) for _ in range(int(input()))]
time_list.sort(key=lambda x: (x[1], x[0]))

end_time = 0
cnt = 0

for start, end in time_list:
    if start >= end_time:
        end_time = end
        cnt += 1

print(cnt)

"""
인프런 강의에 동일한 문제가 있고,
코딩테스트에서도 한번 경험해 봤던 문제였습니다 :)
"""
