#https://school.programmers.co.kr/learn/courses/30/lessons/77485
def solution(rows, columns, queries):
    answer = []
    #행렬 기본값
    rc = []
    num = 1
    for r in range(rows):
        row = []
        for c in range(columns):
            row.append(num)
            num += 1
        rc.append(row)
    #회전
    for query in queries:
        x1 = query[0] - 1   #1
        y1 = query[1] - 1   #1
        x2 = query[2] - 1   #4
        y2 = query[3] - 1   #3
        temp = rc[x1][y1]   #8
        answer1 = temp
        for y in range(y1 + 1, y2 + 1): #2~3    #9~10
            temp1 = rc[x1][y]   #9
            rc[x1][y] = temp    #8
            temp = temp1        #9
            answer1 = min(answer1, temp)
        for x in range(x1 + 1, x2 + 1): #2~4    #16~28
            temp1 = rc[x][y2]   #16
            rc[x][y2] = temp    #10
            temp = temp1        #16
            answer1 = min(answer1, temp)
        for y in range(y2 - 1, y1 - 1, -1): #2~1#27~26
            temp1 = rc[x2][y]   #27
            rc[x2][y] = temp    #28
            temp = temp1        #27
            answer1 = min(answer1, temp)
        for x in range(x2 - 1, x1 - 1, -1): #4~1#20~8
            temp1 = rc[x][y1]   #20
            rc[x][y1] = temp    #26
            temp = temp1        #20
            answer1 = min(answer1, temp)
        answer.append(answer1)
    return answer
