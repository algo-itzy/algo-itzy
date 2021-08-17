"""
# 의석이의 세로로 말해요
세로로 읽은 순서대로 글자들을 출력

첫 번째 줄에 테스트 케이스의 수 T
각 테스트 케이스는 총 다섯 줄
각 줄에는 길이가 1이상 15이하인 문자열
각 문자열은 영어 대문자 ‘A’부터 ‘Z’, 영어 소문자 ‘a’부터 ‘z’, 숫자 ‘0’부터 ‘9’

각 테스트 케이스마다 #T를 출력하고 한 칸을 띄운 후, 의석이가 세로로 읽은 순서대로 글자들을 출력
"""

T = int(input())

for tc in range(1, T + 1):
    ans = ['']*15
    for _ in range(5):
        word = input()
        for i in range(len(word)):
            # ans i 번째에 각 줄의 i번째 문자 배치
            ans[i] += word[i]

    print('#%s %s' % (tc, ''.join(ans)))
