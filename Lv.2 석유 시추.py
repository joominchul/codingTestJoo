#https://school.programmers.co.kr/learn/courses/30/lessons/250136?language=python3
import sys #재귀 한계 확장
sys.setrecursionlimit(1000000)

oil = 0     #석유 덩어리
x_len = 0   #가로 길이
y_len = 0   #세로 길이
#석유 덩어리 탐지(세로, 가로, land, 방문한 좌표 집합, 석유 덩어리의 x좌표 집합)
def detect(y, x, land, visited, m):
    global oil
    #왼쪽, 오른쪽, 위, 아래
    moves = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    #탐지 좌표를 방문하지 않았고, 격자 범위 내에 있고, 석유가 있다면
    if (y, x) not in visited and 0<= y < y_len and 0<= x < x_len and land[y][x] == 1:
        #글로벌 oil에 +1, 방문 집합에 좌표 추가, x좌표 집합에 x좌표 추가
        oil += 1
        visited.add((y, x))
        m.add(x)
        #좌우상하로 좌표를 이동해 탐지
        for move in moves:
            detect(y+move[0], x+move[1], land, visited, m) 
        
def solution(land):
    global oil
    global x_len
    x_len = len(land[0])
    global y_len
    y_len = len(land)
    #x좌표에 따른 시추관을 뚫을 때 뽑을 수 있는 석유 저장 리스트
    ground = [0]*x_len
    #방문 집합
    visited = set()
    #완전 탐색
    for y in range(y_len):
        for x in range(x_len):
            #석유가 있고 아직 방문하지 않았다면
            if (y, x) not in visited and land[y][x] == 1 :
                #석유 덩어리의 x좌표 집합
                m = set()
                detect(y, x, land, visited, m)
                #석유 덩어리가 있는 x좌표에 석유 덩어리 크기 저장
                for i in m:
                    ground[i] += oil
                oil = 0
    return max(ground)
    
