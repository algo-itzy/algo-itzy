from itertools import zip_longest

if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T+1):
        arr = [input() for _ in range(5)]

        print(f"#{tc}", end = " ")

        for i in zip_longest(*arr, fillvalue=""):
            print(*i, sep="", end="")

        print()
            