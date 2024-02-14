#https://school.programmers.co.kr/learn/courses/30/lessons/169199
def findStart(board):               #시작점 찾기
    for yI, y in enumerate(board):
        if("R" in y):
            return [yI, y.index("R")]

def solution(board):                #BFS, 너비 우선 탐색.
    num=0       #길이
    que = []    #탐색을 위한 큐
    R = findStart(board)
    que.append((R[0], R[1], num))   #큐에 시작점 추가
    visit = set()   #방문지
    while (que):
        x, y, num = que.pop(0)      #FIFO
        if (x, y) in visit:         #방문한 곳이면 패스
            continue
        if board[x][y] == "G":      #목표지점이면 길이 리턴
            return num
        visit.add((x, y))           #방문지에 추가
        for mX, mY in ([-1,0], [1,0], [0, -1], [0,1]):  #상하좌우
            nowX, nowY = x, y
            while True:
                nX, nY = nowX+mX, nowY+mY               #상하좌우로 이동
                if 0<=nX<len(board) and 0<=nY<len(board[0]) and board[nX][nY] != "D":
                    nowX, nowY = nX, nY                 #조건에 맞으면 이동
                    continue
                que.append((nowX, nowY, num+1))         #조건에 안 맞으면 큐에 위치 저장 
                break
    
    return -1
