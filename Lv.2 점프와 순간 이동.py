#https://school.programmers.co.kr/learn/courses/30/lessons/12980
def solution(n):    #8분
    ans = 0
    while(n > 2):
        if n % 2 == 1:
            ans += 1
        n //= 2
    return ans + 1
