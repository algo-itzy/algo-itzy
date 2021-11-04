def solution(m, musicinfos):

    dict = {}
    for musicinfo in musicinfos:
        start, end, title, lyrics = musicinfo.split(',')

        tmp = int(end.split(':')[0]) - int(start.split(':')[0])
        play_time = tmp * 60 + int(end.split(':')[1]) - int(start.split(':')[1])

        rearranged = []             # # 붙어있는 애들 때문에 리스트 생성
        for i in range(len(lyrics)):
            if lyrics[i] in 'ABCDEFG':
                if i+1 < len(lyrics) and lyrics[i+1] == '#':
                    if lyrics[i] == 'A':
                        rearranged.append('H')
                    if lyrics[i] == 'C':
                        rearranged.append('I')
                    if lyrics[i] == 'D':
                        rearranged.append('J')
                    if lyrics[i] == 'F':
                        rearranged.append('K')
                    if lyrics[i] == 'G':
                        rearranged.append('L')
                else:
                    rearranged.append(lyrics[i])

        played = ''              # 노래가 재생된 시간만큼 곡 붙여보기
        for i in range(play_time):
            played += rearranged[(i+1) % len(rearranged)-1]

        rearranged_m = []       # 마찬가지로, m 도 # 붙어있는 애들 때문에 리스트 생성
        for i in range(len(m)):
            if m[i] in 'ABCDEFG':
                if i+1 < len(m) and m[i+1] == '#':
                    if m[i] == 'A':
                        rearranged_m.append('H')
                    if m[i] == 'C':
                        rearranged_m.append('I')
                    if m[i] == 'D':
                        rearranged_m.append('J')
                    if m[i] == 'F':
                        rearranged_m.append('K')
                    if m[i] == 'G':
                        rearranged_m.append('L')
                else:
                    rearranged_m.append(m[i])

        played_m = ''
        for i in range(len(rearranged_m)):
            played_m += rearranged_m[(i + 1) % len(rearranged_m) - 1]

        if played_m in played:
            dict[title] = play_time # 노래의 일부분에 해당되면, 딕셔너리에 추가
                                    # 조건: 재생된 시간이 가장 긴 제목 반환, 재생 시간이 같으면 먼저 넣은 제목 반환

    if len(dict) != 0:
        max_key = max(dict, key=dict.get)
        return max_key
    else:                           # 일치하는 음악 없으면
        return "(None)"




# git commit -m "code: Solve programmers 방금그곡 (yeonju)"