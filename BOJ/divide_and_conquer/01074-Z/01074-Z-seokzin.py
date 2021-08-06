n, r, c = map(int, input().split())

res = 0

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