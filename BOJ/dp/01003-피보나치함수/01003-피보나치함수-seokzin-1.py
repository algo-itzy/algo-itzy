t = int(input())

fibo = [1, 0]

for i in range(2, 42):
    fibo.append(fibo[i-1]+fibo[i-2])

for _ in range(t):
    n = int(input())
    print(fibo[n], fibo[n+1])

# 의미 파괴하고 숏코딩한 풀이법 - 이렇게 풀지 말란 뜻