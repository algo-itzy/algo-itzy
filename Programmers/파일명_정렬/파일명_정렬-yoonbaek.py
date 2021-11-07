order = lambda x: (x[0], x[1])

def solution(files: str):
    answer = []
    head_flag, num_flag = False, False
    
    for file in files:
        F = len(file)
        for i in range(len(file)):
            if not head_flag and file[i].isdigit():
                head_flag, head_range = True, i
            if head_flag and not num_flag and not file[i].isdigit():
                num_flag, num_range = True, i
        # num이 끝나고 flag를 갱신하지 못한 경우 == tail이 없는 경우
        if not num_flag:
            num_range = F
        head_flag, num_flag = False, False

        head = file[:head_range].lower()
        num = int(file[head_range:num_range])
        answer.append((head, num, file))

    answer = [x[2] for x in sorted(answer, key=order)]
    return answer

# git commit -m "code: Solve programmers 파일명 정렬 (yoonbaek)"