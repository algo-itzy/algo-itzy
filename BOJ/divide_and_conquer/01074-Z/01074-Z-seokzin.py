n, r, c = map(int, input().split())

res = 0

# 같은 반복문. 대신 4분면구분이 아니라 2조건의 중첩을 통해 계산.
# 직관성 있으나 연산이 2번. 그러나 별 차이 안남
while n > 0:
    h = 2**(n-1) # 리스트 길이의 절반

    if r > h-1:  # r이 리스트의 절반을 넘었는가?
        res += 2*h*h
        r -= h

    if c > h-1:  # c가 리스트의 절반을 넘었는가?
        res += h*h
        c -= h

    n -= 1

print(res)

# 처음에 사분면으로 풀었는데 너무 중복의 느낌이 강했다.
# r와 c는 서로 연관이 없다는 점에 착안해 사분면 없이 풀었다.

# 아래는 Z 문제에 대해 정리했던 제 포스트입니다.
# https://seokzin.tistory.com/entry/%EB%B0%B1%EC%A4%80-1074-Z-%ED%8C%8C%EC%9D%B4%EC%8D%AC