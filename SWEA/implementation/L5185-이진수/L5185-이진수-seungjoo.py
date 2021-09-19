# git commit -m "code: Solve swea L5185 이진수 (seungjoo)"
for test in range(1,int(input())+1):
    N, s = input().split()
    ans = ''
    for i in range(int(N)):
        ans += bin(int(s[i],16))[2:].zfill(4)
    print(f"#{test} {ans}")
