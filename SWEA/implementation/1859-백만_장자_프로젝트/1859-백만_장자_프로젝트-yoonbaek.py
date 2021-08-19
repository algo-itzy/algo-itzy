# solved by YoonBaek
if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T+1):
        N = int(input())
        profits = 0

        prices = list(map(int, input().split()))
        len_prices = len(prices)

        while prices:
            max_idx = max_price = 0
            
            for idx, price in enumerate(prices):
                if price > max_price:
                    max_idx, max_price = idx, price

            for idx in range(max_idx):
                profits += max_price - prices[idx]
            
            prices = prices[max_idx+1:]

        print(f"#{tc} {profits}")