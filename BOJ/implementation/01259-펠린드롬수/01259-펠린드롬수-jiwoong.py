# 반복
from sys import stdin

while True:
    word = str(stdin.readline().strip())
    palin = word[::-1] # 거꾸로 정렬

    if word == '0': # 종료 조건
        break

    if word == palin:
        print('yes')
    else:
        print('no')

# 2

while True:
    word = str(stdin.readline().strip())
    mid = len(word) // 2
    if word == '0':  # 종료 조건
        break
    elif len(word) % 2 != 0:  # 홀수
        word = word.replace(word[mid], '', 1)  # 가운데 수 삭제

    if len(word) % 2 == 0:  # 짝수
        if word[:mid] == word[:mid - 1:-1]:  # 회문 판별
            print('yes')
        else:
            print('no')


"""
git commit -m "code: Solve boj 01259 펠린드롬수 (jiwoong)"
"""