import sys
input = sys.stdin.readline

# 배열에 담아 정렬한 후 피타고라스의 정리를 섰습ㅂ니다.
while 1:
    arr = list(map(int,input().split()))
    if arr == [0,0,0]:
        break
    arr.sort()
    if arr[0]**2 + arr[1]**2 == arr[2]**2:
        print('right')
    else:
        print('wrong')
