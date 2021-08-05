# solved by YoonBaek
from sys import stdin, stdout


print = stdout.write


def input()->list:
    lines = stdin.read().rstrip().split("\n")[1:]
    co_ords = []

    for line in lines:
        x, y = line.split()
        co_ords.append([int(x), int(y)])

    return co_ords


if __name__ == "__main__":
    co_ords = input()
    co_ords.sort(key=lambda x:(x[0], x[1]))

    for x, y in co_ords:
        print(f"{x} {y}\n")