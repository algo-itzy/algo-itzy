import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    clothes = {}  # '옷종류' : 개수로 딕셔너리 생성

    for _ in range(n):
        cloth, cloth_type = input().strip().split()
        if cloth_type not in clothes:
            clothes[cloth_type] = 1
        else:
            clothes[cloth_type] += 1

    ans = 1
    for i in clothes.values():  # 답 = 종류별로 곱 - 1(아무것도 안 입는 것)
        ans *= (i+1)
    print(ans-1)
    
# git commit -m "code: Solve boj 09375 패션왕 신해빈 (seungkyu)"