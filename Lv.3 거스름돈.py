#https://school.programmers.co.kr/learn/courses/30/lessons/12907 
def solution(n, money): 
    #동적 프로그래밍을 위한 경우의 수 저장
    #0~n까지 각 값을 만들 수 있는 경우의 수
    #0원을 만들 수 있는 경우의 수는 1가지임.
    arr = [1] + [0]*n
    #각 화폐별로
    for c in money:
        #c~n원을 만들 수 있는 경우의 수 계산
        for i in range(c, n+1):
            #i원을 만들 수 있는 경우의 수에 i원에서 c원을 뺀 경우의 수를 더해줌.
            arr[i] += arr[i-c]
    return arr.pop() % 1000000007
