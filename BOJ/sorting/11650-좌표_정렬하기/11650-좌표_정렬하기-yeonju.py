"""
x 좌표가 증가하는 순으로
x 좌표가 같으면 y 좌표 증가하는 순으로 정렬 후 출력
1<=N<-100,000
-100,000<=xi,yi<=100,000
"""
import sys

N = int(input()) # 점의 개수 N
num = [] # 좌표값들을 담을 리스트 생성

for _ in range(N):
    num.append(list(map(int,sys.stdin.readline().split()))) #리스트에 좌표값들을 담음

# print(num)
num.sort(key=lambda x:(x[0],x[1])) # x좌표를 기준으로 오름차순으로 배치, x 좌표 값이 같다면 y 좌표를 오름차순으로 정렬


for i in num:
    print(i[0],i[1])



# 이렇게 풀면, key 값이 중복된 경우 다 나중의 value 값으로 덮어지게 된다.

# N = int(input()) # 점의 개수 N
# dict ={} 

# for _ in range(N):
#     X, Y = map(int, input().split())
#     dict[int(X)] = int(Y)

# print(dict)

# # new_dict = sorted(dict.items(), key=lambda x:(x[0],x[1]))
# # print(new_dict)

"""
git commit -m "code: Solve boj 00000 문제 이름 (yeonju)"
"""