import sys

input = sys.stdin.readline
N, M = map(int, input().split())

# 보드 데이터를 매트릭스 형식으로 저장
# 풀이 과정에서 pprint로 출력해보느라 이렇게 만들었습니다.
board = [list(input().strip()) for _ in range(N)]

# 결과값 64로 세팅
min_cnt = 64

# x_idx, y_idx : start index
for y_idx in range(N-7):
    for x_idx in range(M-7):
        
        # 체스판마다 cnt해서 최솟값 갱신
        W_start = 0
        B_start = 0

        for y in range(y_idx, y_idx+8):
            for x in range(x_idx, x_idx+8):
                if (x+y) % 2 == 0:
                    if board[y][x] != 'W':
                        W_start += 1
                    if board[y][x] != 'B':
                        B_start += 1
                else:
                    if board[y][x] != 'B':
                        W_start += 1
                    if board[y][x] != 'W':
                        B_start += 1

        min_cnt = min(min_cnt, W_start, B_start)       

print(min_cnt)


"""
합성곱신경망(CNN)이 생각나는 문제였습니다.
행렬로 된 데이터에 8*8 필터 적용하는 느낌
다 풀고 석진님 코드 봤는데 64-cnt가 있었군요....ㄷㄷㄷㄷ
"""