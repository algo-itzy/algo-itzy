# git commit -m "code: Solve boj 11444 피보나치 수 6 (seungkyu)"
import sys
sys.setrecursionlimit(10**6)

def fibo(n):
    if not fibos.get(n):
        if n % 2:
            k = (n+1)//2
            fibos[n] = (fibo(k)**2 + fibo(k-1)**2)%1000000007
        else:
            k = n//2
            fibos[n] = ((2*fibo(k-1) + fibo(k))*fibo(k))%1000000007

    return fibos[n]

n = int(input())
fibos = {0: 0, 1: 1, 2: 1}
print(fibo(n))