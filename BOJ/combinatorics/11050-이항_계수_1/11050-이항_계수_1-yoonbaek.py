# solved by YoonBaek
# before facts: 84
# after facts: 

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