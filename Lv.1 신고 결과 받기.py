#https://school.programmers.co.kr/learn/courses/30/lessons/92334
def solution(id_list, report, k):
    answer = []
    report_dict = {}    #유저별 신고한 아이디
    report_count = {}   #유저별 신고당한 횟수
    reported = []       #정지될 ID
    for i in id_list:   #딕셔너리들 초기 설정
        report_dict[i] = []
        report_count[i] = 0
    for history in report:
        a, b = history.split(" ")
        if b not in report_dict[a]: #신고하지 않았다면
            report_dict[a].append(b)
            report_count[b] += 1
    for i in report_count:          #정지될 ID 계산
        if report_count[i] >= k:
            reported.append(i)
    for i in id_list:               #각 ID별로
        temp_answer = 0
        for j in report_dict[i]:    #신고한 ID가 
            if j in reported:       #정지되었으면
                temp_answer += 1
        answer.append(temp_answer)
    return answer
