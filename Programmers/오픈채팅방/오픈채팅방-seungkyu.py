# git commit -m "code: Solve programmers 오픈채팅방 (seungkyu)"
def solution(record):
    answer = []
    tmp = []
    users = {}
    for cmds in record:
        cmd = cmds.split()

        if cmd[0] == 'Enter':
            user_id = cmd[1]
            users[user_id] = cmd[2]
            tmp.append(['In', user_id])
        elif cmd[0] == 'Leave':
            user_id = cmd[1]
            tmp.append(['Out', user_id])
        elif cmd[0] == 'Change':
            user_id = cmd[1]
            users[user_id] = cmd[2]
            
    for cmd in tmp:
        if cmd[0] == 'In':
            answer.append(f'{users[cmd[1]]}님이 들어왔습니다.')
        elif cmd[0] == 'Out':
            answer.append(f'{users[cmd[1]]}님이 나갔습니다.')
            
    return answer