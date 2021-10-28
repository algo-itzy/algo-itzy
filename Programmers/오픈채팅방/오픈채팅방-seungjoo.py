# git commit -m "code: Solve programmers 오픈채팅방 (seungjoo)"
def solution(record):
    answer = []
    users = {}
    for log in record:
        command, *user = log.split()
        if command == 'Enter' or command == 'Change':
            user_id, nickname = user
            users[user_id] = nickname
    for log in record:
        command, *user = log.split()
        if command == 'Enter':
            user_id, nickname = user
            answer.append(f'{users[user_id]}님이 들어왔습니다.')
        elif command == 'Leave':
            answer.append(f'{users[user.pop()]}님이 나갔습니다.')

    return answer