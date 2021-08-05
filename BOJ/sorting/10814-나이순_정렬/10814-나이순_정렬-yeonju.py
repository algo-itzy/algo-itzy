"""
회원들의 나이가 증가하는 순으로
나이가 같으면 먼저 가입한 사람이 앞에 
회원 수는 1<=N <-100,000
"""
import sys

N = int(sys.stdin.readline()) # 온라인 저지 회원의 수 
li=[]

for _ in range(N):
    (age,name) = sys.stdin.readline().split()
    li.append(list(int(age),name))

sorted_list =sorted(li, key = lambda x: x[0]) # 어린 순서대로 배열

for i in sorted_list:
    print(i[0],i[1])




"""
git commit -m "code: Solve boj 00000 문제 이름 (yeonju)"
"""