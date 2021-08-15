"""
# 문자열 비교
문자열 str2 안에 str1과 일치하는 부분이 있는지 찾는 프로그램
첫 문자열이 두번째에 존재하면 1, 존재하지 않으면 0을 출력

첫 줄에 테스트 케이스 개수 T가 주어진다.
다음 줄부터 테스트 케이스 별로 길이가 N인 문자열 str1과 길이가 M인 str2가 각각 다른 줄에 주어집니다.

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력
"""

T = int(input())

for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    result = 0
    # 문자열이 str2안에 존재한다면 result 1
    if str1 in str2:
        result = 1
    print(f"#{tc} {result}")