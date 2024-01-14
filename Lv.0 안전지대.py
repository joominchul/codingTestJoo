#https://school.programmers.co.kr/learn/courses/30/lessons/120866
def solution(board):
    bN = len(board)
    # 위험지역을 X로 바꾸고 warning에 +1
    warning = 0
    for x in range(bN):
        for y in range(bN):
            if board[x][y] == 1:
                # 지뢰를 찾으면 warning에 +1
                warning+=1
                if y>0: #좌
                    if board[x][y-1] ==0:
                        board[x][y-1] = 'X'
                        warning+=1
                if y<(bN-1): #우
                    if board[x][y+1] ==0:
                        board[x][y+1] = 'X'
                        warning+=1
                if x>0: #상
                    if board[x-1][y] == 0:
                        board[x-1][y] = 'X'
                        warning+=1
                    if y>0: #좌상
                        if board[x-1][y-1] == 0:
                            board[x-1][y-1] = 'X'
                            warning+=1
                    if y<(bN-1): #우상
                        if board[x-1][y+1] == 0:
                            board[x-1][y+1] = 'X'
                            warning+=1
                if x<(bN-1):#하
                    if board[x+1][y] == 0:
                        board[x+1][y] = 'X'
                        warning+=1
                    if y>0:#좌하
                        if board[x+1][y-1] == 0:
                            board[x+1][y-1] = 'X'
                            warning+=1
                    if y<(bN-1):#우하
                        if board[x+1][y+1] == 0:
                            board[x+1][y+1] = 'X'
                            warning+=1
    answer = (bN*bN) - warning
    return answer
