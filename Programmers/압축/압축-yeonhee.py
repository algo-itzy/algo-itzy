def solution(msg):
    dic = {}
    answer = []

    for i in range(26):
        dic[chr(65 + i)] = i + 1

    left = 0
    right = 0
    cnt = 27

    while right <= len(msg):
        string = msg[left:right+1]
        if string in dic.keys():
            right += 1
        else:
            answer.append(dic[msg[left:right]])
            dic[msg[left:right+1]] = cnt
            cnt += 1
            left = right
    answer.append(dic[msg[left:right]])
    return answer


print(solution('KAKAO'))
print(solution('TOBEORNOTTOBEORTOBEORNOT'))
print(solution('ABABABABABABABAB'))
