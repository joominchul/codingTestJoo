#https://school.programmers.co.kr/learn/courses/30/lessons/155651
def timeCheck(time):#표기법 확인
    minute = time%100
    if minute > 59: #분이 59분을 초과하면
        time = time - 60 + 100 #60을 빼고 1시간을 추가함
    return time
def solution(book_time):
    answer = 0
    book_time.sort()
    room = [0]
    book_check = False
    for b in book_time:
        for r in range(len(room)):
            if((int(b[0][0:2])*100 + int(b[0][3:])) >= room[r]):#예약 시작 시간이 객실 사용 가능 시간보다 크면
                time = int(b[1][0:2])*100 + int(b[1][3:]) + 10 #객실 사용 가능 시간 갱신
                room[r] = timeCheck(time)  #시간 표기 확인
                book_check = True #예약 성공
                break
        if not book_check: #예약 실패 시
            time = int(b[1][0:2])*100 + int(b[1][3:]) + 10 #객실 사용 가능 시간 갱신
            room.append(timeCheck(time)) #객실 추가
        book_check = False #예약 여부 초기화
    answer = len(room)
    return answer
