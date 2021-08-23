for test in range(1,int(input())+1):
    N, M, L = map(int, input().split())
    arr = list(map(int, input().split()))
    flag = 1
    for _ in range(M):
        command = input().split()
        if command[0] == 'I':
            arr.insert(int(command[1]),int(command[2]))
        elif command[0] == 'D':
            if not arr:
                flag=0
                break
            arr.pop(int(command[1]))
        else:
            arr[int(command[1])] = int(command[2])
    if len(arr) > L:
        if flag:
            print(f'#{test} {arr[L]}')
        else:
            print(f'#{test} -1')
    else:
        print(f'#{test} -1')
