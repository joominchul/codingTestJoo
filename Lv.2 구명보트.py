#https://school.programmers.co.kr/learn/courses/30/lessons/42885
from collections import deque
def solution(people, limit):
    answer = 0
    p = deque()
    people.sort()
    for i in people:
        p.append(i)
    
    while(p):
        answer += 1
        if len(p) > 1 and p[-1] + p[0] <= limit:
            p.pop()
            p.popleft()
        else:
            p.pop()
    return answer
