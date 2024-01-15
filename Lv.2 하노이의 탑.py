#https://school.programmers.co.kr/learn/courses/30/lessons/12946
def hanoi(n, s, e): #n, 시작 원판, 이동 원판
    Sum = s+e
    if n==1:
        return [[s,e]]
    else:
        if Sum == 4:    #시작과 이동이 1,3 
            return hanoi(n-1, s, 2) + [[s,e]] + hanoi(n-1, 2, e)
        elif Sum == 3:  #시작과 이동이 1,2
            return hanoi(n-1, s, 3) + [[s,e]] + hanoi(n-1, 3, e)
        else:           #시작과 이동이 2,3 
            return hanoi(n-1, s, 1) + [[s,e]] + hanoi(n-1, 1, e)
def solution(n):
    answer = [[]]
    answer = hanoi(n, 1, 3)
    return answer
