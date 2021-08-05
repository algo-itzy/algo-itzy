# solved by YoonBaek
# before facts: 84
# after facts: 76
# 큰 차이는 아니니 알고리즘 테스트에서는 
# 시간초과 뜨지 않는 이상 그냥 풀자
# 숫자가 커지면 써야 함


facts = []
for _ in range(10+1):
    facts += [0]


def factorial(n: int)->int:
    facts[0] = facts[1] = 1
    for val in range(2,n+1):
        if not facts[val]:
            facts[val] = val * facts[val-1]
 
    return facts[n]


def combination(n: int, k: int)->int:
    return factorial(n) // (factorial(n-k)*factorial(k))


if __name__ == "__main__":
    n, k = list(map(int, input().split()))

    print(combination(n,k))