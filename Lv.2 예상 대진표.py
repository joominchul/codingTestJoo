#https://school.programmers.co.kr/learn/courses/30/lessons/12985
def solution(n,a,b):
    answer = 0
    while(a != b):
        if a % 2 != 0:
            a += 1
        if b % 2 != 0:
            b += 1
        a = a/2
        b = b/2
        answer += 1

    return answer
