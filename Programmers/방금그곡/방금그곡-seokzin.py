def solution(m, musicinfos):
    
    def del_sharp(s):
        s = s.replace('C#', 'c')
        s = s.replace('D#', 'd')
        s = s.replace('F#', 'f')
        s = s.replace('G#', 'g')
        s = s.replace('A#', 'a')   
        return s 


    def full_song(t, song):
        tmp = [''] * t

        for i in range(t):
            tmp[i] = song[i % len(song)]
        return ''.join(tmp)


    def get_sec(s):
        min, sec = s.split(':')
        return int(min)*60 + int(sec)


    answer = ['', 0]  # 반환 조건을 맞추기 위해 길이값 함께 저장

    for info in musicinfos:
        s, e, title, song = info.split(',')
        m = del_sharp(m)
        song = del_sharp(song)
        t = get_sec(e) - get_sec(s)  # 재생시간

        fullsong = full_song(t, song)

        if m in fullsong:
            if t > answer[1]:
                answer = [title, t]

    return answer[0] if answer[0] else "(None)"