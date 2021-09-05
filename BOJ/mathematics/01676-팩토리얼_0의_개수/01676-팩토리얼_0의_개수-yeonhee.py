from math import factorial

n = factorial(int(input()))
cnt = 0

while not n%10:
    n = n//10
    cnt += 1

print(cnt)
