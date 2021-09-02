expr = input().split('-')
result = sum(map(int, expr[0].split('+')))

for exp in expr[1:]:
    result -= sum(map(int, exp.split('+')))

print(result)
