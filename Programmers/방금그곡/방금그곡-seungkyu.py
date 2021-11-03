# git commit -m "code: Solve programmers 방금그곡 (seungkyu)"
def solution(m, musicinfos):
    answer = ''
    dic = {}

    for musicinfo in musicinfos:
        start, end, title, music = musicinfo.split(',')
        a, b = start.split(':')
        c, d = end.split(':')
        
        tmp = []
        i = 0

        while i < len(music):
            if music[i].isalpha():
                if i < len(music)-1 and music[i+1] == '#':
                    tmp.append(music[i]+'#')
                    i += 2
                else:
                    tmp.append(music[i])
                    i += 1        
        time = (int(c) - int(a))*60 + (int(d) - int(b))

        dic[title] = [time, (time//len(tmp))*tmp + tmp[:time%len(tmp)]]

    ans = []
    len_m = 0

    for i in m:
        if i.isalpha():
            len_m += 1
            
    for title, music in dic.items():
        for i in range(len(music[1])-len_m+1):
            if ''.join(music[1][i:i+len_m]) == m:
                ans.append([title, music[0]])
                break
    
    ans = sorted(ans, key=lambda music: -music[1])

    if ans:
        answer = ans[0][0]
    else:
        answer = "(None)"

    return answer
