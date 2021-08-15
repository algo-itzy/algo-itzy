"""
# 종이붙이기
가로 x 세로 길이가 10x20, 20x20인 직사각형 종이
교실 바닥에 20xN 크기의 직사각형을 테이프로 표시하고, 이 안에 준비한 종이를 빈틈없이 붙이는 방법
종이를 붙이는 모든 경우를 찾으려면 테이프로 만든 표시한 영역을 몇 개나 만들어야 되는지 계산

테스트 케이스 개수 T
테스트 케이스 별로 N

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력
"""


def paper(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    return paper(n - 1) + (2 * paper(n - 2))


T = int(input())
for t in range(1, T + 1):
    n = int(input()) // 10
    print(f"#{t} {paper(n)}")
