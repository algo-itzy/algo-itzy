# git commit -m "code: Solve programmers 오픈채팅방 (jiwoong)"
def solution(record):
    dict = {}
    arr = []
    for user in record:
        word = user.split(" ")
        if word[0] == "Enter":
            dict[word[1]] = word[2]
            arr.append([word[1], "님이 들어왔습니다."])
        elif word[0] == "Leave":
            arr.append([word[1], "님이 나갔습니다."])
        elif word[0] == "Change":
            dict[word[1]] = word[2]
    result = []
    for i, j in arr:
        result.append(dict[i] + j)
    return result
