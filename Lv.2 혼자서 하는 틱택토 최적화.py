#https://school.programmers.co.kr/learn/courses/30/lessons/160585
def wincheck(player, board):                            #빙고 확인
    for i in range(3):
        if all(b == player for b in board[i]):          #가로 빙고
            return True
        if all(board[j][i] == player for j in range(3)):#세로 빙고
            return True
    
    if all(board[i][i] == player for i in range(3)):    #대각선 빙고
        return True
    if all(board[2-i][i] == player for i in range(3)):
        return True
    else:
        return False
def solution(board):
    answer = 1
    first = sum(i.count("O") for i in board)            #O의 개수
    second = sum(i.count("X") for i in board)           #X의 개수
    
    if first < second or first>second+1 or (wincheck("O", board) and first == second) or (wincheck("X", board) and first > second):
                                                        #O보다 X의 개수가 많거나, O가 X+1보다 많거나,
                                                        #O가 이겼는데 O와 X의 개수가 같거나,
                                                        #X가 이겼는데 O가 X보다 많으면 틀림
        answer = 0
    
    return answer
