#https://school.programmers.co.kr/learn/courses/30/lessons/120868
def solution(sides):
    answer = sides[0] + sides[1] - max(sides) - 1 + min(sides)
    return answer
