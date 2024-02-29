#https://school.programmers.co.kr/learn/courses/30/lessons/86053
def check(a, b, g, s, w, t, time): #주어진 time에 금과 은을 전달할 수 있는지 확인. 결정 문제
    total = 0   #도시에서 조달할 수 있는 총 양
    tg = 0      #도시에서 조달할 수 있는 금의 양
    ts = 0      #도시에서 조달할 수 있는 은의 양
    n = len(g)
    for i in range(n):
        count = ((time//t[i])//2) + ((time//t[i])%2)
        tg+=min(g[i], count*w[i])           #도시의 금 양과 운반 양 중 작은 것.
        ts+=min(s[i], count*w[i])           #도시의 은 양과 운반 양 중 작은 것.
        total+=min(w[i]*count, g[i]+s[i])   #자원의 총량과 운반 양 중 작은 것
    if total >= (a+b) and tg >= a and ts >= b: 
        return True
    else:
        return False
    
def solution(a, b, g, s, w, t):
    low = 0                 #최소 시간. a와 b가 모두 0이면
    high = 2*(a+b)*max(t)   #최대 시간. 왕복 * 자원량 * 가장 긴 운반 시간 / 1
    while low <= high:      #이진 탐색
        if low+1 == high:
            return high
        middle = (low + high)//2
        if check(a, b, g, s, w, t, middle):
            high = middle
        else:
            low = middle
