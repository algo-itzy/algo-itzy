def same(x):
    x = int(x)    # string 으로 들어오기 때문에 int 타입으로 감싸주기
    if x% 2 == 0: # 짝수인 애들은 1을 빼줘서, (1 과 2) (3과 4)... 괄호끼리 같은 값으로 만들어주기 
        x -= 1

    return x

t = int(input())

for tc in range(t):
    n = int(input())            # 돌아가야 할 학생 수 n
    visited = [0]*401           # 1 ~ 400 방 만들어주기 
    info = [list(map(same, input().split())) for _ in range(n)]

    for contents in info:
        x, y = contents        # 현재 놀러간 방 x,  돌아가야하는 방 y 
        if x > y:              # range 에 넣기 위해, 작은 수 - 큰 수 순서로 재배열 
            x, y = y, x
        for j in range(x, y+1): # 특정 방 앞을 지났으면 +1 
            visited[j] += 1     # visited 중 max 의 값이 최소 단위 시간

    print(f'#{tc+1} {max(visited)}')



# 아래는 안 읽으셔도 돼요! 처음 할 때 실패한 것,,,, ㅠ-ㅠ
# t = int(input())
#
# for tc in range(t):
#     n = int(input()) # 돌아가야 할 학생 수 n
#
#     info = [list(map(int, input().split())) for _ in range(n)]
#     cnt = 1
#     for i in range(n):
#         for j in range(i+1, n):
#             if info[j][0] <= info[i][0] <= info[j][1] or info[j][1] <= info[i][0] <= info[j][0]
#                     or info[j][0] <= info[i][1] <= info[j][1] or info[j][1]<= info[i][1] <= info[j][0]:
#                 cnt +=1
#
#     print(f'#{tc+1} {cnt}')

