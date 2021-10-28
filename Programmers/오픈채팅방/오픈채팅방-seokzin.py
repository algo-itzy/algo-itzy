def solution(records):
    answer = []
    dic = {}

    for record in records:
        r = record.split()
        
        if r[0] in ("Enter", "Change"):
            dic[r[1]] = r[2]

    for record in records:
        r = record.split()
        
        if r[0] == 'Enter':
            answer.append(f'{dic[r[1]]}님이 들어왔습니다.')
        elif r[0] == 'Leave':
            answer.append(f'{dic[r[1]]}님이 나갔습니다.')
    
    return answer