import sys
input = sys.stdin.readline

N,M = map(int,input().split())
not_hear_list = {input().rstrip():1 for _ in range(N)}
not_human=[]
for _ in range(M):
    not_see = input().rstrip()
    try:
        if not_hear_list[not_see]:
            not_human.append(not_see)
    except:
        continue
# 사전순 출력을 위한 정렬
not_human.sort()
print(len(not_human))
for human in not_human:
    print(human)