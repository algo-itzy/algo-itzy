def solution(files):
    answer = []

    for file in files:
        head, number, tail = '', '', ''

        for i in range(len(file)):
            if file[i].isdigit():  # 숫자 전까지 HEAD
                head = file[:i]
                file = file[i:]
                break

        for j in range(len(file)):
            if not file[j].isdigit():
                number = file[:j]
                tail = file[j:]
                break
        else:  # TAIL이 없을 떄 처리
            number = file

        answer.append((head, number, tail))

    answer.sort(key=lambda x: (x[0].upper(), int(x[1])))

    return [''.join(x) for x in answer]