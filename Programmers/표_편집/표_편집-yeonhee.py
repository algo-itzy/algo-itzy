def solution(n, k, cmds):
    answer = ['O'] * n
    linked_list = {i: [i-1, i+1] for i in range(1, n+1)}
    stack = []

    k += 1

    for cmd in cmds:
        cmd = cmd.split(' ')
        if cmd[0] == 'U':
            for _ in range(int(cmd[1])):
                k = linked_list[k][0]

        elif cmd[0] == 'D':
            for _ in range(int(cmd[1])):
                k = linked_list[k][1]

        elif cmd[0] == 'C':
            up, down = linked_list[k]
            stack.append([up, down, k])
            answer[k-1] = 'X'
            if down == n+1:
                k = linked_list[k][0]
            else:
                k = linked_list[k][1]

            if up == 0:  # Head일 경우
                linked_list[down][0] = up
            elif down == n+1:  # Tail일 경우
                linked_list[up][1] = down
            else:
                linked_list[up][1] = down
                linked_list[down][0] = up

        elif cmd[0] == 'Z':
            up, down, now = stack.pop()
            answer[now-1] = 'O'

            if up == 0:
                linked_list[down][0] = now
            elif down == n+1:
                linked_list[up][1] = now
            else:
                linked_list[up][1] = now
                linked_list[down][0] = now

    return ''.join(answer)


print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))
