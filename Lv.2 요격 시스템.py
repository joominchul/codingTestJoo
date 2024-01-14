#https://school.programmers.co.kr/learn/courses/30/lessons/181188
def solution(targets):
    answer=0
    targets.sort()  #오름차순 정렬
    bound = 0       #폭격 미사일 경계
    for i in targets:
        if bound <= i[0]:   #미사일 경계보다 시작점이 크거나 같으면
            answer+=1       #요격 미사일 추가
            bound = i[1]    #경계 갱신
        if bound >i[1]:     #경계보다 끝점이 작으면
            bound = i[1]    #경계 갱신
    return answer
