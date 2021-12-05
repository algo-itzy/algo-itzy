# git commit -m "code: Solve boj 01629 곱셈 (seungkyu)"
def powpow(b):
    if b == 1:
        return a%c

    tmp = powpow(b//2)
    tmp = tmp*tmp%c

    if b % 2 == 0:
        return tmp
    else:
        return a*tmp%c

a, b, c = map(int, input().split())
print(powpow(b))