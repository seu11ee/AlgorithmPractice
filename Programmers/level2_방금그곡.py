def solution(m, musicinfos):
    answer = []
    idx = 0
    for info in musicinfos:

        play_start,play_end,song_title,song = info.split(",")
        song_info = []
        listen = []
        for i in song:
            if i == "#":
                song_info[-1] += "#"
            else:
                song_info.append(i)
        for i in m:
            if i == "#":
                listen[-1] += "#"
            else:
                listen.append(i)
        play_time = calculate_time(play_start,play_end)
        play = ["" for _ in range(play_time+len(listen))]
        for i in range(play_time):
            play[i] = song_info[i%(len(song_info))]
            for i in range(0,play_time-len(listen)+1):
                if play[i:i+len(listen)] == listen:
                    answer.append((play_time,song_title,idx))
                    idx+=1
                    break
    if len(answer) == 0:
        return "(None)"
    answer.sort(key = lambda x : (-x[0],x[2]))
    return answer[0][1]

def calculate_time(start,end):
    start_hour,start_min = map(int,start.split(":"))
    end_hour,end_min = map(int,end.split(":"))
    m = end_min - start_min
    if m < 0:
        end_hour -= 1
        m = 60 + m
    h = end_hour - start_hour
    return 60*h+m

print(solution("ABCDEFG",["12:50,13:04,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B",["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC",["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))