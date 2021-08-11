import sys
input = sys.stdin.readline

N, M = map(int, input().split())

person_d = {}  # 듣도 못한 사람 저장
person_both = []  # 두 경우 모두 해당할 때만 저장

for i in range(N):
    person_d[input().strip()] = 1

for _ in range(M):
    person = input().strip()

    if person in person_d:  # 두 경우 모두 해당될 때
        person_both.append(person)  # 저장
        
person_both.sort()  # 사전 순으로 정렬

# 답 출력
print(len(person_both))
for person in person_both:
    print(person)
