# Solved by YoonBaek
import sys

def isVPS() -> str :
    # init stack
    stack = 0
    parenthesises = sys.stdin.readline()
    # stack process
    for p in parenthesises :
        if p == "(" :
            stack += 1
        elif p == ")" :
            stack -= 1
        if stack < 0 :
            break

    # get the result
    if stack == 0 :
        print("YES")
    else :
        print("NO")

T = int(input())

for _ in range(T) :
    isVPS()