def solution(records):
    answer = []
    members = {}
    cmds = []

    for record in records:
        record = record.split()

        if record[0] == "Leave":
            cmd, pk = record

        else:
            cmd, pk, nickname = record
            members[pk] = nickname

        if cmd != 'Change':
            cmds.append((cmd, pk))

    for cmd, pk in cmds:
        message = "님이 들어왔습니다." if cmd == "Enter" else "님이 나갔습니다."
        answer.append(f"{members[pk]}{message}")
    
    return answer
    
# git commit -m "code: Solve programmers 오픈채팅방 (yoonbaek)"