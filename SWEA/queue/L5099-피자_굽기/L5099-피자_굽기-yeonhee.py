import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    pizza = list(map(int, input().split()))
    cheese = [[i+1, pizza[i]] for i in range(n)]   # 치즈의 높이와 인덱스 번호

    i = 0
    while len(cheese) > 1:
        tmp = cheese.pop(0)
        tmp[1] //= 2

        if not tmp[1]:  # 치즈 다 녹았으면
            if i + n < m:   # 넣을 피자가 남아있으면
                cheese.append([n+i+1, pizza[n+i]])
                i += 1

        else:  # 치즈 안녹았으면 다시 넣기
            cheese.append(tmp)

    print(f'#{t} {cheese[0][0]}')

"""
이유는 모르겠는데 같은 코드로 enumerate 쓰면
테스트케이스 하나가 에러납니다.

알고리즘 틀린 줄알고 억울..
"""