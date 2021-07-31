import sys

N,M = map(int, sys.stdin.readline().split())
chess = [sys.stdin.readline().rstrip() for _ in range(N)]

# 8*8 체스판 세팅
min_repaint = 64

for i in range(N-7): #시작하는 좌표
    for j in range(M-7): #시작
        count_w = 0 #짝수가 화이트
        count_b = 0 #짝수가 블랙

        for h in range(i, i+8): #체스판 8*8 둘러보기
            for w in range(j, j+8):
                if (h+w) % 2 == 0 : # 좌표의 합 더해서 짝수이면 (0,0) . (0,2) 
                    if chess[h][w] != 'W':
                        count_w += 1
                    if chess[h][w] != 'B':
                        count_b += 1
                else:
                    if chess[h][w] != 'B':
                        count_w += 1
                    if chess[h][w] != 'W':
                        count_b += 1

        # min(iterable)- 괄호( ) 안에 리스트, 문자 열 등 반복 가능한 자료형을 넣으면 가장 작은 값을 반환

        min_repaint = min(min_repaint, count_b, count_w) 

print(min_repaint)