num1, num2 = map(int, input().split())

factor1 = set([i for i in range(1, num1+1) if num1%i == 0])
factor2 = set([i for i in range(1, num2+1) if num2%i == 0])

gcd = max(factor1 & factor2)  # 최대공약수
print(gcd)
print(int(num1 * num2 / gcd))  # 최소공배수


"""
git commit -m "code: Solve boj 02609 최대공약수와 최소공배수 (yeonhee)"
"""