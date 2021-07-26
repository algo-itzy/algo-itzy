# solved by YoonBaek
import sys

def solve() :
    words = sys.stdin.readline()
    reverse = words[::-1]
    
    print(" ".join(reverse.split()[::-1]))

if __name__ == '__main__':
    T = int(input())

    for _ in range(T) :
        solve()