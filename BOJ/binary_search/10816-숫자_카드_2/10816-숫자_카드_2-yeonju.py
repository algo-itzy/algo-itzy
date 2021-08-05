"""
첫째 줄에는 상근이가 갖고 있는 카드의 개수 - N
둘째 줄에는 카드에 직현 정수(-10,000,000<= <=10,000,000
셋째 줄에는 상근이가 몇 개 갖고 있는지 구해야할 정수의 개수 - M
넷째 줄에는 그 수들. 각 정수의 범위는 위와 동일
"""

# 딕셔너리를 사용해서 풀이 
N= int(input())
sanggun = sorted(list(map(int, input().split())))
M = int(input())
given = list(map(int, input().split()))

dic = {}
for i in sanggun:
    try:
        dic[i] +=1      # 딕셔너리에 key 값이 있었으면 1을 추가
    except:             # 딕셔너리에 key 값이 없으면 추가하고 + value 에 1 넣음 
        dic[i] = 1

for j in given:
    try:
        print(dic[j], end = " ") # 각각의 인덱스에 해당하는 딕셔너리 key 의 value 값을 프린트
    except:
        print(0, end = " ") # 상근이한테 해당 카드가 없었다면, 0을 출력


# 아래 방법은 시간 초과....
# N= int(input())
# sanggun = list(map(int, input().split()))
# M = int(input())
# given = list(map(int, input().split()))

# for i in range(M):
#     print(sanggun.count(given[i]),end=' ')



"""
git commit -m "code: Solve boj 00000 문제 이름 (yeonju)"
"""