import sys
input = sys.stdin.readline

for test in range(int(input())):
    H,W,N = map(int,input().split())
    room = ''
    # 꼭대기층이 아닌경우와 꼭대기층인경우에 따라 가로값, 세로값 계산 방식이 다르다.
    # 0처리를위해 문자열로 연산했다.
    if N%H:
        room += str(N%H)
        if N//H>=9:
            room += str(N//H+1)
        else:
            room += '0'+str(N//H+1)
    else:
        room += str(H)
        if N//H>=10:
            room += str(N//H)
        else:
            room += '0'+str(N//H)
    print(room)
