#https://school.programmers.co.kr/learn/courses/30/lessons/49191
def solution(n, results):
    answer = 0
    #선수 별 승패 딕셔너리 초기 설정
    player = {}
    for i in range(n):
        player[i+1] = [set(), set()] #키가 이긴 선수 목록, 진 선수 목록
    #승패 딕셔너리 내용 채우기
    for re in results:
        win = re[0]
        lose = re[1]
        player[win][0].add(lose)
        player[lose][1].add(win)
    #실력에 따라 승패 예측
    for key in player:
        #키를 이긴 선수는 키가 이긴 선수들도 이길 수 있음
        for winner in player[key][1]:
            player[winner][0].update(player[key][0])
        #키가 이긴 선수는 키가 진 선수들도 이길 수 없음
        for loser in player[key][0]:
            player[loser][1].update(player[key][1])
    #순위가 확정적인 선수 체크
    for key in player:
        if(len(player[key][0]) + len(player[key][1]) == n - 1):
            answer += 1
    return answer
