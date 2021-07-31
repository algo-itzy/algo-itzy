N = int(input())
numbers = list(map(int, input().split()))

# 소수가 아닌 숫자 count
not_prime = 0

for number in numbers:
    if number == 1:
        not_prime += 1
    elif number == 2:
        continue
    else:
        for i in range(2, number):
            if number % i == 0:
                not_prime += 1
                break

print(N - not_prime)