t = int(input())

zero = [1, 0]
one = [0, 1]

for i in range(2, 41):
    zero.append(zero[i-1]+zero[i-2])
    one.append(one[i-1]+one[i-2])

for _ in range(t):
    n = int(input())
    print(zero[n], one[n])

# 여러 테스트 케이스가 주어지기 때문에 초기에 fibo 값 테이블을 만든다.
# zero와 one은 비슷하지만 다른 데이터입니다. 그래서 따로 두는 것이 더 의미 있다고 봅니다.