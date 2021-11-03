# git commit -m "code: Solve programmers 방금그곡 (seungjoo)"
parse_set = {'C#': 'a', 'D#': 'b', 'F#': 'c', 'G#': 'd', 'A#': 'e', 'E#': 'k'}

def parse_scale(music):
    parsed = []
    for idx in range(len(music)):
        if music[idx] == '#':
            parsed.append(parse_set[parsed.pop()+music[idx]])
        else:
            parsed.append(music[idx])
    return ''.join(parsed)

def make_time(time):
    a, b = time.split(':')
    return int(a) * 60 + int(b)

def solution(m, musicinfos):
    answer, play_time = '', 0
    m = parse_scale(m)
    for play in musicinfos:
        start, end, title, music = play.split(',')
        start, end, music = make_time(start), make_time(end), parse_scale(music)
        length, total_length = len(music), end - start
        music = music * (total_length // length) + music[:total_length % length]
        if play_time < total_length and m in music:
            answer = title
            play_time = total_length
    return answer if answer else '(None)'