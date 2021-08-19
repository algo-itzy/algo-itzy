import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T+1):

    N = int(input())
    
    rooms = []
    ans = 0
    for i in range(N):
        rooms.append(list(map(int, input().split())))
    
    indices = [0]*200
    
    for room in rooms:
        # 오른쪽에서 왼쪽으로 이동하는 경우가 있어서 모두 왼->오로 이동하도록 설정
        if room[0] > room[1]:
            room[0], room[1] = room[1], room[0]
        # 방의 위치 인덱스 = (방num-1) // 2
        cur, res = (room[0]-1)//2, (room[1]-1)//2
        for i in range(cur, res+1):
            indices[i] += 1

    print(f'#{test_case} {max(indices)}')