#https://school.programmers.co.kr/learn/courses/30/lessons/72413
def solution(n, s, a, b, fares):
    answer = 0
    short = []
    for i in range(n):                      #n*n의 2차원 배열 생성. 
        temp = [-1]*n                       #기본값으로 연결되지 않았다는 걸 의미하는 -1 설정
        short.append(temp)
    for fare in fares:                      #short 배열에 택시 요금 추가
        short[fare[0]-1][fare[1]-1] = fare[2]
        short[fare[1]-1][fare[0]-1] = fare[2]
    #플로이드 알고리즘
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if short[i][k] != -1 and short[k][j] != -1: #경유지로 가는 경로가 있다면
                    if short[i][j] == -1:   #i에서 j까지 바로 가는 경로가 없었다면
                        short[i][j] = short[i][k]+short[k][j]#경유지를 추가한 경로를 추가.
                    else:                   #기존 경로가 있었다면 경유지 경로 비교 후 최소 경로로 변경.
                        short[i][j] = min(short[i][k]+short[k][j], short[i][j])
    for i in range(n):                      #자기 자신 경로는 0으로 설정
        short[i][i] = 0
    answer = short[s-1][a-1]+short[s-1][b-1]#A와 B가 각각 택시를 탔을 경우
    for i in range(n):                      #지점 수만큼 경유지 경로 확인
                                            #만약 출발지에서 i지점, i지점에서 A지점, 
                                            #i지점에서 B지점으로 가는 경로가 있다면
        if short[s-1][i] != -1 and short[i][a-1] != -1 and short[i][b-1] != -1:
            temp = short[s-1][i] + short[i][a-1] + short[i][b-1]
            answer = min(answer, temp)      #기존 경로와 i경유지 추가 경로를 비교 후 최소 경로로 변경.
    return answer
