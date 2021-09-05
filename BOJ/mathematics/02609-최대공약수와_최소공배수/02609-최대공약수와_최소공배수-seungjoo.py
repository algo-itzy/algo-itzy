import sys
input = sys.stdin.readline

# 유클리드 호제법 이었나..?
def gcd(a,b):
    if a<b:
        a,b=b,a
    while a%b:
        a=a%b
        a,b=b,a
    return b

num_a,num_b = map(int,input().split())

min_common = gcd(num_a,num_b)
max_common = (num_a//min_common)*(num_b//min_common)*min_common

print(min_common)
print(max_common)