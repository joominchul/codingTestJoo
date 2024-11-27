#https://school.programmers.co.kr/learn/courses/30/lessons/87946
from itertools import permutations
def solution(k, dungeons):
    answer = -1
    #순열들을 탐색
    for per in list(permutations(dungeons)):
        temp_answer = 0
        temp_k = k
        for dungeon in per:
            if(temp_k>=dungeon[0]):
                temp_k -= dungeon[1]
                temp_answer += 1
        answer = max(answer, temp_answer)
    return answer
