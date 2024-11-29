#https://school.programmers.co.kr/learn/courses/30/lessons/138476
def solution(k, tangerine):
    answer = 0
    #크기별 귤을 저장할 딕셔너리
    guul = {}
    for t in tangerine:
        temp = guul.get(t)
        if(temp):
            guul[t] += 1
        else:
            guul[t] = 1
    #각 타입 별 귤의 개수를 저장할 리스트
    t_list = []
    for g in guul:
        t_list.append(guul[g])
    #귤 개수가 많은 것부터 상자에 담기귤 개수가 많은 것부터 상자에 담기
    t_list = sorted(t_list)
    for i in range(len(t_list) - 1, -1, -1):
        if(k > 0):
            answer += 1
            k -= t_list[i]
        else:
            break
    return answer
