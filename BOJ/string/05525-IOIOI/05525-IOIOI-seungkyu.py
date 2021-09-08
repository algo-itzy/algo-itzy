import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().strip()

cnt, io_num, i = 0, 0, 0

while i < M-2:
  # 3단어씩 검사 
  if S[i] == 'I' and S[i+1] == 'O' and S[i+2] == 'I':
    io_num += 1  # IOI 찾으면 패턴개수를 +1
    if io_num == N:  # 패턴 N개면 답 +1 
      io_num -= 1
      cnt += 1   
    i += 2  # 인덱스 +2
  else:  # IOI아닐 때는 인덱스 1개씩 증가시키면서 검사
    io_num = 0
    i += 1  
  
print(cnt)

# git commit -m "code: Solve boj 05525 IOIOI (seungkyu)"