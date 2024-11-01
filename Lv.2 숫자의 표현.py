#https://school.programmers.co.kr/learn/courses/30/lessons/12924
def solution(n):
    answer = 0
    #1부터 n까지
    for i in range(1,n+1):
        temp = 0
        for j in range(i, n+1):
            temp += j
            #더한 값이 n이면 정답에 추가
            if temp == n:
                answer += 1
                break
            #더한 값이 n보다 크면 j로 시작하는 자연수들로 표현 불가
            if temp > n:
                break
    return answer
