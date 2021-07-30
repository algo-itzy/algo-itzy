while True:
    data = input().strip()
    if data == '0':
        break
    print('yes' if data == data[::-1] else 'no')


"""
git commit -m "code: Solve boj 01259 펠린드롬수 (yeonhee)"
신박한 풀이를 고민했는데 신박한게 안나오네요..
"""