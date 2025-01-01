#https://school.programmers.co.kr/learn/courses/30/lessons/17679
def solution(m, n, board):
    answer = 0
    board_copy = []
    #보드 복사본 만들기
    for x in range(m):
        board_copy.append([])
        for y in range(n):
            board_copy[x].append(board[x][y])
    while(True):
        same = set()
        #없앨 수 있는 블럭들 찾기
        for x in range(m - 1):
            for y in range(n - 1):
                if board_copy[x][y] != "0" and board_copy[x][y] == board_copy[x + 1][y] == board_copy[x][y + 1] == board_copy[x + 1][y + 1]:
                    same.add((x, y))
                    same.add((x + 1, y))
                    same.add((x, y + 1))
                    same.add((x + 1, y + 1))
        #각 열 별 없어지는 블럭 딕셔너리 만들기
        same_dict = {}
        for x, y in same:
            if y in same_dict:
                same_dict[y].append(x)
            else:
                same_dict[y] = [x]
        #빈칸 내리기
        for y in range(n):
            if y not in same_dict:
                continue
            for x in range(m - 1, -1, -1):
                count = 0
                for h in same_dict[y]:
                    if x < h:
                        count += 1
                board_copy[x + count][y] = board_copy[x][y]
                if count != 0:
                    board_copy[x][y] = "0"
        temp = len(same)
        answer += temp
        if temp == 0:
            break
    return answer
