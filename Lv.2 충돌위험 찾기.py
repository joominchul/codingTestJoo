#https://school.programmers.co.kr/learn/courses/30/lessons/340211
def solution(points, routes):
    answer = 0
    point_dict = {}
    robot_route_list = []
    for i in range(len(points)):    #번호 별 포인트 딕셔너리 설정
        point_dict[i + 1] = points[i]
    for i in range(len(routes)):            #로봇의 이동 경로를 구함
        robot_route = []
        start = point_dict[routes[i][0]].copy() #copy 안 해주면 point_dict 값도 변경됨.
        for j in range(1, len(routes[i])):
            end = point_dict[routes[i][j]].copy()   #운송 경로에 따라 end 변경
            while start[0] != end[0]:
                temp = start.copy()             #copy 안 해주면 robot_route에 추가한 리스트 값도 변경됨.
                robot_route.append(temp)
                if end[0] > start[0]:
                    start[0] += 1
                else:
                    start[0] -= 1
            while start[1] != end[1]:
                temp = start.copy()
                robot_route.append(temp)
                if end[1] > start[1]:
                    start[1] += 1
                else:
                    start[1] -= 1
        
        robot_route.append(start)
        robot_route_list.append(robot_route)    #로봇 운송 경로를 robot_route_list에 저장
    empty = 0               #리스트가 비었는지 확인하는 변수
    while empty != len(routes):  #robot_route_list가 모두 비면 종료
        robot_position = [] #동시간 로봇 위치
        danger = []         #위험 상황 좌표
        empty = 0           
        for r in robot_route_list:
            if len(r) == 0: #리스트가 비었으면
                empty += 1
                continue
            position = r.pop(0)
            if position in robot_position and position not in danger:   #로봇이 서로 겹치면서 기존 위험 상황이 아닌 경우
                danger.append(position)
                answer += 1
            else:
                robot_position.append(position)
    return answer
