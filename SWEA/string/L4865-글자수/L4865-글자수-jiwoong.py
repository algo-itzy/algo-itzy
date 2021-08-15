"""
# 글자수
문자열 str1에 포함된 글자들이 str2에 몇 개씩 들어있는지 찾고, 그중 가장 많은 글자의 개수를 출력

첫 줄에 테스트 케이스 개수 T가 주어진다.
다음 줄부터 테스트 케이스 별로 길이가 N인 문자열 str1과 길이가 M인 str2가 각각 다른 줄에 주어진다.

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력
"""

T = int(input())

for tc in range(1, T + 1):
    str1 = input()
    str2 = input()

    cnt = {}

    for i in str1:
        cnt[i] = 0

    for j in str2:
        if j in str1:
            cnt[j] += 1

    ans = 0
    for value in cnt.values():
        if value > ans:
            ans = value

    print(f'#{tc} {ans}')
