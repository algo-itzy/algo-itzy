def time_to_min(s, e):
    sh, sm = map(int, s.split(':'))
    eh, em = map(int, e.split(':'))
    start, end = sh * 60 + sm, eh * 60 + em
    return end - start


def sharp_to_lower(codes):
    codes = codes.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
    return codes


def solution(m, musicinfos):
    answer = [0, '(None)']  # 재생된 시간, title
    m = sharp_to_lower(m)

    for info in musicinfos:
        start, end, title, codes = info.split(',')
        playtime = time_to_min(start, end)
        codes = sharp_to_lower(codes)
        a, b = divmod(playtime, len(codes))
        played_codes = codes * a + codes[:b]
        if m in played_codes and playtime > answer[0]:
            answer = [playtime, title]

    return answer[1]


print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
