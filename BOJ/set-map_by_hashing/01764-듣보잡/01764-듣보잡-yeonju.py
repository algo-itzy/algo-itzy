import sys

input = sys.stdin.readline

N, M = map(int, input().split())    # 듣도 못한 사람 수 N, 보도 못한 사람 수 M 
                                    # N, M 은 500,000 이하 자연수 

heard = set()
saw = set()
for i in range(N):
    heard.add(input())

# print(heard)

for j in range(M):
    saw.add(input())

# print(saw)
results = heard & saw   # 교집합 원소들만 담은 배열 results 

ans =list(results)      # set 은 순서가 없어서, 순서를 매기고 싶으면 list 로 감싸줘야 함
ans.sort()

print(len(ans))          # 듣도 보도 못한 사람 수 출력

for i in range(len(ans)):
    print(ans[i][:-1])


# list 로 하면 시간 초과가 나서 set() 으로 구현
# set 에서는 append() 대신 add

#     # for person in heard:
# #     if person in saw:
# #         results.append(person)
