#https://school.programmers.co.kr/learn/courses/30/lessons/12914
def solution(n):
    answer = 0
    jump = [0]*(n+1)
    jump[0] = 1
    jump[1] = 1
    for i in range(2, n+1):
        jump[i] = jump[i-1] + jump[i-2]
    return jump[n]%1234567
