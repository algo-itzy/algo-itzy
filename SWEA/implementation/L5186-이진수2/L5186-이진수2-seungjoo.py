# git commit -m "code: Solve swea L5186 이진수2 (seungjoo)"
def binary(n,depth):
    if depth>13:
        return '2'
    if not n:
        return ''
    if n >= 2**(-depth):
        n -= 2**(-depth)
        return '1' + binary(n,depth+1)
    return '0' + binary(n,depth+1)


for test in range(1,int(input())+1):
    N = float(input())
    ans = binary(N,1)
    if ans[-1]=='2':
        ans = 'overflow'
    print(f'#{test} {ans}')