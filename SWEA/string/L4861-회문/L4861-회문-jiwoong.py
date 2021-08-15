"""
# 회문
NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력
가로 뿐만 아니라 세로로 찾아질 수도 있다.

첫 줄에 테스트 케이스 개수 T가 주어진다.
다음 줄부터 테스트케이스의 첫 줄에 N과 M이 주어진다.
다음 줄부터 N개의 글자를 가진 N개의 줄이 주어진다.

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력
"""

# def row_search(N, M, arr):
#     palindrome = []
#     for r in range(N):
#         for c in range(N - M + 1):
#             if arr[r][c: c + M] == arr[r][c: c + M][::-1]:
#                 palindrome.append(arr[r][c: c + M])
#                 return palindrome[0]  # 회문을 찾으면 함수 종료하고 return
#
#
# # 세로 탐색
# def column_search(N, M, arr):
#     palindrome = []
#     for r in range(N - M + 1):  # 세로방향 확인하기
#         for c in range(N):
#             col_lst = []
#             for i in range(M):
#                 col_lst.append(arr[r + i][c])  # 세로방향 문자열 만들기
#             if col_lst == col_lst[::-1]:
#                 palindrome.append(''.join(col_lst))
#                 return palindrome[0]
#
#
# T = int(input())
# for tc in range(T + 1):
#     N, M = map(int, input().split())
#
#     # 테이블 입력
#     arr = []
#     for _ in range(N):
#         arr.append(input())  # 원래 격자, 가로 검색용
#
#     # 탐색
#     palindrome = row_search(N, M, arr)
#     if palindrome is None: palindrome = column_search(N, M, arr)
#     print(f"#{tc} {palindrome}")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    ans = ''

    # row
    pal = 0
    for i in range(N):
        for j in range(N - M + 1):
            for k in range(M // 2):
                if arr[i][j + k] == arr[i][j + M - 1 - k]:
                    pal += 1
            if pal == M // 2:
                for l in range(j, j + M):
                    ans += arr[i][l]
            pal = 0

    # col
    pal = 0
    for j in range(N):
        for i in range(N - M + 1):
            for k in range(M // 2):
                if arr[i + k][j] == arr[i + M - 1 - k][j]:
                    pal += 1
            if pal == M // 2:
                for l in range(i, i + M):
                    ans += arr[l][j]
            pal = 0

    print(f"#{tc} {ans}")
