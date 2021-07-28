import sys

N = int(sys.stdin.readline())

queue = []

for i in range (N) :
    cmd = sys.stdin.readline().split() # 입력 받은 명령을 공백을 기준으로 나눠서 cmd에 넣음
    
    if cmd[0] == 'push' : # 큐에 입력 받은 정수를 넣음, 출력하진 않음
        queue.insert(0, cmd[1])

    elif cmd[0] == 'pop' :
        if len(queue) != 0 :  # 큐에서 가장 앞에 있는 정수를 빼고 출력
            print(queue.pop())
        else : print(-1) 

    elif cmd[0] == 'size' :
        print(len(queue)) # 큐의 정수의 개수를 출력

    elif cmd[0] == 'empty' :
        if len(queue) == 0 : # 큐가 비어있으면 1, 없으면 0 출력
            print(1)
        else : 
            print(0)

    elif cmd[0] == 'front' :
        if len(queue) == 0 : print(-1)
        else :
            print(queue[len(queue) -1 ]) # 큐의 가장 앞에 있는 정수를 출력 

    elif cmd[0] == 'back' :
        if len(queue) == 0: 
            print(-1)
        else : 
            print(queue[0]) # 큐의 가장 뒤에 있는 정수 출력



    # front - 가장 처음에 추가된 요소임으로, 리스트의 맨 뒤의 원소를 출력해야 함
    # back - 가장 마지막에 추가된 요소임으로, 리스트의 0번째 요소를 출력해야 함