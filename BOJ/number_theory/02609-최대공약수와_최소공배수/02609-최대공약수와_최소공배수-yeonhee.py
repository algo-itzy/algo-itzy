num1, num2 = map(int, input().split())

factor1 = set([i for i in range(1, num1+1) if num1%i == 0])
factor2 = set([i for i in range(1, num2+1) if num2%i == 0])

# 최대공약수 : set의 교집합을 이용한 풀이
gcd = max(factor1 & factor2)
print(gcd)

# 최소공배수 : 위에서 구한 최대공약수를 이용한 풀이
print(int(num1 * num2 / gcd))

