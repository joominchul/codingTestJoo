#https://school.programmers.co.kr/learn/courses/30/lessons/12945
def solution(n):
    answer = 0
    fibo_list = [0, 1]
    for i in range(2, n + 1):
        fibo_list.append(fibo_list[i-1] + fibo_list[i-2])
    answer = fibo_list[n]
    return answer % 1234567
