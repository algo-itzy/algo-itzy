# solved by YoonBaek
import sys

def solve() :
    words = sys.stdin.readline()
    # 전체 뒤집기
    reverse = words[::-1]
    
    # 공백별로 나누고 순서 바꾸기
    print(" ".join(reverse.split()[::-1]))

if __name__ == '__main__':
    T = int(input())

    for _ in range(T) :
        solve()