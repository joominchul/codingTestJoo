#https://school.programmers.co.kr/learn/courses/30/lessons/150370
def cal_month(year, month, day): #유효기간을 더한 날짜를 알맞게 설정
    if day == 1:
        month -= 1
        day = 28
    else:
        day -= 1
    while month > 12:       #유효기간을 더한 월을 알맞게 설정
        month -= 12
        year += 1
    if month == 0:
        month = 12
        year -= 1
    return [year, month, day]
def solution(today, terms, privacies):
    answer = []
    term_dict = {}
    num = 0 #개인정보 번호
    today_year, today_month, today_day = map(int, today.split(".")) #today 년, 월, 일 추출.
    for term in terms:      #약관 딕셔너리 설정
        term_type, period = term.split(" ")
        term_dict[term_type] = int(period)
    for privacy in privacies:
        num += 1
        date, term = privacy.split(" ")
        year, month, day = map(int, date.split("."))
        date_list = cal_month(year, month + term_dict[term], day)  #유효기간 더함
        year = date_list[0]
        month = date_list[1]
        day = date_list[2]
        if year < today_year:   #유효기간 지났는지 확인.
            answer.append(num)
        if year == today_year:
            if month < today_month:
                answer.append(num)
            if month == today_month:
                if day < today_day:
                    answer.append(num)
    answer.sort()
    return answer
