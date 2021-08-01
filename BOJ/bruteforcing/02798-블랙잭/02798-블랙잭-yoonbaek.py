# solved by YoonBaek
"""
그냥 무지성으로 BruteForce로 풀어도 풀리고
성능도 나쁘지 않습니다.
다만, 정렬 후 투입을 통해 break로 bruteforcing을 줄일 수 있습니다.
"""

def solve() -> int:
    Max = 10

    for one in range(n-2):
        for two in range(one+1, n-1):
            for three in range(two+1, n):
                total = cards[one]+cards[two]+cards[three]

                # total이 m보다 작으면 max인지만 확인하고 종료합니다. 
                if total <= m:
                    Max = total if total > Max else Max 
                    break

    return Max

if __name__ == "__main__":
    n, m = map(int, input().split())
    cards = list(map(int, input().split()))
    # solve에서 연산을 줄이기 위해 뒤집어 줍니다.
    cards = sorted(cards, reverse=True)

    print(solve())

