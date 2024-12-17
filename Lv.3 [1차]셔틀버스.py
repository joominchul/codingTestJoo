#https://school.programmers.co.kr/learn/courses/30/lessons/17678?language=python3
#시각을 분 단위로 변경
def chTime(timetable):
    new_timetable = []
    for t in timetable:
        temp = int(t[0:2]) * 60 + int(t[3:])
        new_timetable.append(temp)
    return sorted(new_timetable)
#분 단위를 시각으로 변경
def chAnswer(start_time):
    if(start_time // 60 < 10):
        temp = '0' + str(start_time // 60)
    else:
        temp = str(start_time // 60)
    if(start_time % 60 < 10):
        temp1 = '0' + str(start_time % 60)
    else:
        temp1 = str(start_time % 60)
    return temp + ':' + temp1
def solution(n, t, m, timetable):
    origin_len = len(timetable) #줄 선 크루 수
    timetable = chTime(timetable)
    start_time = 540 - t #09:00 - t
    count = 0
    last_crew = 540   #마지막에 셔틀에 탄 크루의 도착 시각(분 단위)
    #셔틀 개수 별로
    for i in range(n):
        start_time += t
        count = 0   #탈 수 있는 정원
        for time in timetable.copy():
            if time <= start_time and count < m:    #탈 수 있으면
                last_crew = timetable.pop(0)
                count += 1
            else:
                break
    #버스에 탈 수 있으면
    if count < m:  
        return chAnswer(start_time)
    return chAnswer(last_crew - 1)
