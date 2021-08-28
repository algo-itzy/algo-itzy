N = int(input())
p = list(map(int, input().split()))
waiting = 0
result = 0

for i in sorted(p):
    waiting += i
    result += waiting

print(result)

"""
오랜만에 행복한 문제네요...
"""
