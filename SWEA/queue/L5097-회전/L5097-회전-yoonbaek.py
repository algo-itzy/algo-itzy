inputs = lambda : map(int, input().split())

if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T+1):
        N, M = inputs()
        print(f"#{tc} {list(inputs())[M%N]}")
