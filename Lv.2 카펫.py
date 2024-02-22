#https://school.programmers.co.kr/learn/courses/30/lessons/42842#
def solution(brown, yellow):
    for i in range(1, int(yellow**0.5)+1):  #1 ~ 루트 옐로우 + 1
        if yellow % i == 0:                 #i가 옐로우의 약수일 때
            x = yellow/i                    #옐로우의 가로
            y = i                           #옐로우의 세로
            if brown == (x*2 + y*2 + 4):    #브라운과 비교해 맞으면
                return [x+2, y+2]           #리턴
