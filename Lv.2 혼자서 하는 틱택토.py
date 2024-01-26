def solution(board):
    answer = 1
    first = 0   #O 개수
    second = 0  #X 개수
    fwin = 0    #O 빙고 개수
    swin = 0    #X 빙고 개수
    for i in range(3):
        if board[i] == "OOO":
            fwin+=1
        if board[i] == "XXX":
            swin+=1
        if board[0][i] == board[1][i] == board[2][i] == "O":
            fwin+=1
        if board[0][i] == board[1][i] == board[2][i] == "X":
            swin+=1
        for j in range(3):
            if board[i][j] == "O":
                first+=1
            if board[i][j] == "X":
                second+=1
    if board[0][0] == board[1][1] == board[2][2] == "O":
        fwin+=1
    if board[0][0] == board[1][1] == board[2][2] == "X":
        swin+=1
    if board[2][0] == board[1][1] == board[0][2] == "O": 
        fwin+=1
    if board[2][0] == board[1][1] == board[0][2] == "X": 
        swin+=1
    if first < second or first>second+1 or (fwin > 0 and first == second) or (swin > 0 and first > second):
        answer = 0
    
    return answer
