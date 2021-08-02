# Solved by YoonBaek
from sys import stdin, stdout

input = stdin.readline
print = stdout.write

def solve(h: int, w: int, n: int) -> str:
    room_num = n//h+ 1
    floor = n%h
    if not floor:
        room_num -= 1
        floor = h

    return f"{floor}{room_num:02}\n" 

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        h, w, n = map(int, input().split())
    
        print(solve(h,w,n))