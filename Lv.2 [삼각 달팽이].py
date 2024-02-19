#https://school.programmers.co.kr/learn/courses/30/lessons/68645
def solution(n):
    answer = [[0] * i for i in range(1, n+1)]   #삼각형 모양으로 2차원 리스트 생성
    num=1
    mx = [1, 0, -1] #x 좌표값 변경 값 리스트
    my = [0, 1, -1] #y 좌표값 변경 값 리스트
    m = 0           #좌표 변경 값
    x = -1
    y = 0
    for i in range(n):
        for j in range(i, n):   #이동 거리가 점차 줄어듬
            m = i % 3           #좌표 변경 값 변경
            x += mx[m]          #x 좌표 변경
            y += my[m]          #y 좌표 변경
            answer[x][y] = num
            num+=1
    return sum(answer,[])       #2차원 리스트들 합침
