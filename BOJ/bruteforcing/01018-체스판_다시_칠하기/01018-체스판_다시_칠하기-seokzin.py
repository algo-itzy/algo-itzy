n, m = map(int, input().split())
board = []
res = 64 # 색칠할 최소값 - 64로 초기화

for _ in range(n):
  line = input()
  board.append(line)

for i in range(n-7): # 시작 y좌표
  for j in range(m-7): # 시작 x좌표
    cnt = 0
    
    # 시작 좌표로부터 8*8 칸 탐색
    for y in range(i, i+8):
      for x in range(j, j+8):
        # BW판과 비교
        if ((y+x) % 2 == 0 and board[y][x] == 'B') or ((y+x) % 2 == 1 and board[y][x] == 'W'): 
          cnt += 1
        
    # WB판은 BW판과 반전 관계니 64-cnt 하면 된다. 따로 구할 필요 X
    res = min(res, cnt, 64-cnt)
    
print(res)