# git commit -m "code: Solve programmers 방금그곡 (jiwoong)"
def timeGet(s, e):
    sh, sm = s.split(":")  # 시작 시, 분
    eh, em = e.split(":")  # 종료 시, 분
    m = int(em) - int(sm)  # 분
    h = int(eh) - int(sh)  # 시
    m += h * 60  # 시간 분으로 환산
    return m


def getMelodyList(melody):
    ml = []
    me = ""
    melody_len = len(melody)
    for i in range(melody_len):
        if melody[i] == "#":
            ml.append(me)
            me = ""
            continue
        me += melody[i]
        if i != melody_len - 1:
            if melody[i + 1] == "#":
                me += melody[i + 1]
            else:
                ml.append(me)
                me = ""
        else:
            ml.append(melody[i])
    return ml


def solution(m, music_info):
    ans = []
    for info in music_info:
        s, e, name, melody = info.split(',')
        time = timeGet(s, e)
        melody_list = getMelodyList(melody)
        print(melody_list)
        arr = ""
        for i in range(time):
            arr += melody_list[i % len(melody_list)]
        arr = arr.replace(m + "#", "-")
        arr = arr.replace(m, "!")
        if arr.find("!") >= 0:
            ans.append((name, time))
    if not ans:
        return "(None)"
    ans.sort(key=lambda x: -x[1])  # 시간 순 정렬 후 가장 큰 시간
    return ans[0][0]
