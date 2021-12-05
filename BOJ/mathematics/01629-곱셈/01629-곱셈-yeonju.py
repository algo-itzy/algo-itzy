def power(a, n):
    if n == 1:
        return a % c
    else:
        tmp = power(a, n//2)
        if n % 2 == 0:
            return (tmp * tmp) % c
        else:
            return (tmp * tmp * a) % c


a, b, c = map(int, input().split())
print(power(a, b))

# git commit -m "code: Solve boj 01629 곱셈 (yeonju)"