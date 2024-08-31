#https://school.programmers.co.kr/learn/courses/30/lessons/12978
def solution(N, road, K):
    answer = 0
    short = []
    INF = 50*10000 + 1      #걸리는 시간 최대값
    for i in range(N):      #n*n의 2차원 배열 생성. 
        temp = [INF]*N      #최대값을 기본값으로
        short.append(temp)
    for r in road:          #배열에 걸리는 시간의 최솟값 저장
        short[r[0]-1][r[1]-1] = min(short[r[0]-1][r[1]-1], r[2])
        short[r[1]-1][r[0]-1] = min(short[r[1]-1][r[0]-1], r[2])
            
    #플로이드 알고리즘
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if(i == j): #제자리일 경우
                    short[i][j] = 0
                else:       #돌아가는 길과 직선 길 중 더 짧게 걸리는 길을 저장
                    short[i][j] = min(short[i][k]+short[k][j], short[i][j])
    
    for v in short[0]:      #배달 가능 마을 구함
        if v <= K:
            answer += 1
    return answer
