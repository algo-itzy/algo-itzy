
import sys
input = sys.stdin.readline

# eval쓸라그랬는데 0으로 시작하는 숫자있어서 실패..
expression = input().split('-')
new_expression = []
for ex in expression:
    nums = ex.split('+')
    sum_n = 0
    for num in nums:
        sum_n += int(num)
    new_expression.append(sum_n)
print(2*new_expression[0] - sum(new_expression))