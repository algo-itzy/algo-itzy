while True:
    # 변의 길이가 정렬되지 않았을 때를 대비
    a, b, c = sorted(map(int, input().split()))
    if c == 0:
        break
    print('right' if c**2 == a**2 + b**2 else 'wrong')