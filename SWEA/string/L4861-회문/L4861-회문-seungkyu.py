import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T+1):

    N, M = map(int, input().split())
    words =[]
    for _ in range(N):
        words.append(input())
    
    # 가로로 검사
    for i in range(N):
        for j in range(N-M+1):
            word = words[i][j:j+M]

            if word == word[::-1]:  # 회문 검사
                print(f'#{test_case}', word)

    # 세로로 검사
    for i in range(N):
        for j in range(N-M+1):
            word = ''  # 세로 검사는 쉽게 슬라이싱되지 않아 새로 변수 선언
            for k in range(M):
                word += words[j+k][i]

            if word == word[::-1]:  # 회문 검사
                print(f'#{test_case}', word)
