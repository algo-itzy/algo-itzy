import sys
input = sys.stdin.readline

for test in range(int(input())):
    p = input().rstrip()
    n = int(input())
    xi = input().rstrip()[1:-1].split(',')
    if not n and 'D' in p:
        print('error')
        continue
    reverse_x = 0
    left = 0
    right = len(xi)-1
    for command in p:
        if command == 'R':
            reverse_x ^= 1
        else:
            if left <= right:
                if reverse_x:
                    right -= 1
                else:
                    left += 1
            else:
                print('error')
                break
    else:
        if reverse_x:
            print(f"[{','.join(xi[left:right+1][::-1])}]")
        else:
            print(f"[{','.join(xi[left:right+1])}]")