def solution(m, musicinfos):
    def parse_time(time: str):
        hour, minute = time.split(':')
        return 60*int(hour) + int(minute)


    def parse_note(song:str):
        parsed_song = ''
        song_len = len(song)
        for i in range(song_len):
            if not song[i] == "#":
                note = song[i]
                if i != song_len-1 and song[i+1] == "#":
                    note = note.lower()
                parsed_song += note
        return parsed_song
        

    m = parse_note(m)
    max_runtime, answer = 0, ''
    
    for info in musicinfos:
        start, end, title, song = info.split(',')
        start, end = map(parse_time, (start, end))
        runtime = end-start

        song, song_len = parse_note(song), len(song)

        actual_song = ''
        for i in range(runtime):
            actual_song += song[i%song_len]

        if m in actual_song and runtime > max_runtime:
            max_runtime = runtime
            answer = title
                        
    return answer if answer else "(None)"

# git commit -m "code: Solve programmers 방금그곡 (yoonbaek)"