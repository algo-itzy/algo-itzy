"""
# 어디에 단어가 들어갈 수 있을까
N X N 크기의 단어 퍼즐
특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력

첫 줄에 총 테스트 케이스의 개수 T
다음 줄부터 각 테스트 케이스
테스트 케이스의 첫 번째 줄에는 단어 퍼즐의 가로, 세로 길이 N 과, 단어의 길이 K
테스트 케이스의 두 번째 줄부터 퍼즐의 모양 2차원 정보
퍼즐의 각 셀 중, 흰색 부분은 1, 검은색 부분은 0

테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력
"""

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    # 가로
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 1:  # 1 만나면 cnt 1 더함
                cnt += 1
            else:  # 0 만나면 초기화
                if cnt == K:
                    ans += 1
                cnt = 0
        if cnt == K:
            ans += 1

    # 세로
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[j][i] == 1:
                cnt += 1
            else:
                if cnt == K:
                    ans += 1
                cnt = 0
        if cnt == K:
            ans += 1

    print(f"#{tc} {ans}")
