# 파이썬 집합 메서드 연습
import sys

read = sys.stdin.readline
write = sys.stdout.write

if __name__ == "__main__":
    N = int(read())
    S = set()
    all = set(map(str, range(1, 21)))

    for _ in range(N):
        cmd = read().split()
        if len(cmd) == 2:
            val = cmd[1]
        cmd = cmd[0]

        if cmd == "add":
            S.add(val)
        elif cmd == "remove":
            # safe delete
            S.discard(val)
        elif cmd == "check":
            write(f"{1 if val in S else 0}\n")
        elif cmd == "toggle":
            S.remove(val) if val in S else S.add(val)
        elif cmd == "all":
            S = all
        elif cmd == "empty":
            S = set()
