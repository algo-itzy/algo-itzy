def solution(record):
    users = {}
    records = []

    for event in record:
        event = event.split()
        action, userid = event[0], event[1]
        if action in ("Enter", "Change"):
            users[userid] = event[2]
        records.append((userid, action))

    answer = []

    for userid, action in records:
        if action == 'Enter':
            answer.append(f'{users[userid]}님이 들어왔습니다.')
        if action == 'Leave':
            answer.append(f'{users[userid]}님이 나갔습니다.')

    return answer
