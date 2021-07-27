# push : 정수 X를 큐에 넣음
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 출력.
# size: 큐에 들어있는 정수의 개수 출력
# empty: 큐가 비어있으면 1, 아니면 0을 출력
# front: 큐의 가장 앞에 있는 정수를 출력.
# back: 큐의 가장 뒤에 있는 정수를 출력.
# 정수가 없을 때 -1 출력

n = int(input())
que = []  # input 받아서 que 리스트 지정하기

for i in range(n):  # sys는 아직 더 공부해야 할 거 같아서 우선 문제는 풀어봤어요
    num = input().split()
    if num[0] == 'push':
        que.append(num[1])
    elif num[0] == 'pop':
        if len(que) != 0:
            print(que.pop(0))
        else:
            print(-1)
    elif num[0] == 'size':
        print(len(que))
    elif num[0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif num[0] == 'front':
        if len(que) != 0:
            print(que[0])
        else:
            print(-1)
    elif num[0] == 'back':
        if len(que) != 0:
            print(que[-1])
        else:
            print(-1)  # 시간 초과 뜨네요 sys로 나중에 해보겠습니다
