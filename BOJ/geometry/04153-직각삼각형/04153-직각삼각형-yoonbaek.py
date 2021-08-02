# solved by YoonBaek
from sys import stdin, stdout

input = stdin.readline
print = stdout.write

def is_pyth(a, b, c):
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b

    if a**2 + b**2 == c**2:
        return "right\n"

    return "wrong\n"
        

if __name__ == "__main__":
    
    while True:
        a, b, c = map(int, input().split())
    
        if a == b == c == 0:
            break
        print(is_pyth(a, b, c))