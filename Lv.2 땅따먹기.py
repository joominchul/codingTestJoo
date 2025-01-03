#https://school.programmers.co.kr/learn/courses/30/lessons/12913
def solution(land):
    answer = 0
    for i in range(1, len(land)):
        for j in range(4):
            temp = land[i - 1].copy()
            temp.pop(j)
            land[i][j] += max(temp)
    
    return max(land[len(land)-1])
