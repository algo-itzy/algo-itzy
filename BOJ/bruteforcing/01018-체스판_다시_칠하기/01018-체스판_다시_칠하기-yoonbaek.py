from sys import stdin

# Solved by YoonBaek
"""
Task 구상.
1. Case of B
      01234 
    0 BWBWB...
    1 WBWBW...
    2 BWBWB...
    홀홀 짝짝 -> b
    짝홀 홀짝 -> w ... xor 인데?
2. Compare each case with input by bruteforcing
3. Case 1 vs Case 2 Compare
4. Print min.
5. 8 by 8 이라는걸 뒤늦게 읽음 왠지 tc1 만 맞더라
6. 8 by 8 커널 cnn 인줄
"""

if __name__ == "__main__":
    board = stdin.read().rstrip().split("\n")
    N,M = map(int, board.pop(0).split())
    
    # global cnt
    min = 64

    for n in range(N-7): # 정사각형 세로
        for m in range(M-7): # 정사각형 가로
            # rollback b case min
            # 실제 b min은 아니고 w min일 수도 있습니다
            b_min = 0

            for row in range(8):
                for col in range(8):
                    if row%2 ^ col%2:
                        if board[row+n][col+m] == "W":
                            b_min += 1
                    else: 
                        if board[row+n][col+m] == "B":
                            b_min += 1
            # b - w compare 
            cur_min = b_min if b_min < 64-b_min else 64-b_min
            # update global min
            min = min if min < cur_min else cur_min

    # get result
    print(min)
    