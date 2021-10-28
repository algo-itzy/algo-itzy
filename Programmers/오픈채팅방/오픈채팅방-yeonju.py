def solution(record):
    answer = []
    dict = {}

    for i in record:    # change 반영한 최종 닉네임과 아이디값 없데이트
        if i.split()[0] != 'Leave':
            key_ = i.split()[1]
            dict[key_] = i.split()[2]

    for i in record:
        key_ = i.split()[1]
        if i.split()[0] == 'Enter':
            answer.append(dict[key_] + '님이 들어왔습니다.')

        if i.split()[0] == 'Leave':
            answer.append(dict[key_] + '님이 나갔습니다.')

    return answer


solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])

# git commit -m "code: Solve programmers 오픈채팅방 (yeonju)"