## 30점 코드
from math import ceil
def solution(m, musicinfos):
    for music in musicinfos:
        music = music.split(',')
        time1 = music[0].split(':')
        time2 = music[1].split(':')
        if time1[0]<time2[0]:
            hour = int(time2[0])-int(time1[0])
            minutes = 60*hour-int(time1[1])
            time = minutes + int(time2[1]) 
        else:
            time = int(time2[1])-int(time1[1])
        origin = (music[3]*ceil(time/len(music[3].replace('#', ''))))[:time+music[3].count('#')]
        
        if m in origin:
            if origin.split(m)[1][0] != '#':
                return music[2]