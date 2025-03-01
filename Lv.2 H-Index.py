#https://school.programmers.co.kr/learn/courses/30/lessons/42747?language=python3
def solution(citations):
    answer = 0
    citations.sort()                #검색 속도를 빠르게 하기 위해 오름차순 정렬
    while answer <= citations[-1]:  #가장 인용 횟수가 많은 논문까지 검사
        count = 0
        for cita in citations:      #answer번 이상 인용된 논문이 answer번 이상인지 검사
            if cita >= answer:      #answer번 이상 인용됐는지 확인
                count += 1
                if count >= answer: #인용된 논문이 answer번 이상이면 answer +1
                    answer += 1
                    break
        else:                       #answer번 미만이면 검사 종료
            break
    return answer - 1               #마지막 answer에서 1을 빼줌
