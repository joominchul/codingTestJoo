#https://school.programmers.co.kr/learn/courses/30/lessons/43105 
def solution(triangle):
    height = len(triangle)      #삼각형의 높이
    for x in range(1, height):  #1차(1~높이-1)
        for y in range(x+1):    #2차(0~높이-1)
            if 0<y<x:           #삼각형 가장자리가 아닐 때
                triangle[x][y] = max(triangle[x-1][y-1], triangle[x-1][y]) + triangle[x][y]
            elif y==0:          #삼각형 왼쪽 가장자리
                triangle[x][y] = triangle[x-1][y] + triangle[x][y]
            else:               #삼각형 오른쪽 가장자리
                triangle[x][y] = triangle[x-1][y-1] + triangle[x][y]
    answer = max(triangle[-1])
    return answer
