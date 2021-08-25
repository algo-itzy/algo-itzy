for tc in range(1, int(input())+1):
    N, M, L = map(int, input().split())	
    arr = list(map(int, input().split()))

    for _ in range(M) :
        cmd = list(input().split())

        if cmd[0] == 'I':
            arr.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == 'C':
            arr[int(cmd[1])] = int(cmd[2])
        elif cmd[0] == 'D':
            arr.pop(int(cmd[1]))
    
    print(f"#{tc}", arr[L] if L < len(arr) else -1)