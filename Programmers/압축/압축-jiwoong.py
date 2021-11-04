# git commit -m "code: Solve programmers 압축 (jiwoong)"
import string


def solution(msg):
    # ASCII 코드 대문자로
    dic = dict([(x, i + 1) for i, x in enumerate(string.ascii_uppercase)])
    num = 26
    answer = []
    msg_len = len(msg)
    check = ""
    for i in range(0, msg_len):
        if i == msg_len - 1:  # 마지막 글자
            answer.append(dic[check + msg[i]])
            break
        check += msg[i]
        if check + msg[i + 1] in dic:  # 딕셔너리에 있으면
            continue
        else:  # 없으면
            num += 1
            dic[check + msg[i + 1]] = num
            answer.append(dic[check])
            check = ""
    return answer
