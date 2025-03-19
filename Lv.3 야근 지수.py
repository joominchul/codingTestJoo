#https://school.programmers.co.kr/learn/courses/30/lessons/12927?language=python3
import heapq

def solution(n, works):
    answer = 0
    if sum(works) <= n:
        return 0
    works = [-work for work in works]
    heapq.heapify(works)
    while n > 0:
        max_work = heapq.heappop(works) #최대값 꺼냄
        max_work += 1                   # 1 감소
        heapq.heappush(works, max_work) # 다시 삽입
        n -= 1
    for n in works:                     #야근 지수 계산
        answer += (n*n)
    return answer
