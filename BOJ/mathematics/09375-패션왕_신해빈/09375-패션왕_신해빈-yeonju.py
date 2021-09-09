t = int(input())

for tc in range(t):
    n = int(input())

    clothes = dict()        # 옷의 종류와 갯수를 담을 딕셔너리 선언
    for i in range(n):
        name ,type = map(str, input().split())

        if type in clothes.keys():  # hat 인지 turban 인지 중요 x, 카테고리만 중요
            clothes[type] += 1
        else:
            clothes[type] = 1

    ans = 1
    for i in clothes.keys():
        ans *= clothes[i] +1

    print(ans-1)                    # 아무것도 안 입는 경우는 제외


# 프로그래머스에서 봤던 문제네요,,

        
    
# git commit -m "code: Solve boj 09375 패션왕 신해빈 (yeonju)"