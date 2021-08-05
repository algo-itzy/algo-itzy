from math import factorial # 팩토리얼을 사용 

N, K = list(map(int, input().split())) 

print(factorial(N)//(factorial(K) * factorial(N-K))) 

"""
git commit -m "code: Solve boj 00000 문제 이름 (yeonju)"
"""