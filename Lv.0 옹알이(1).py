#https://school.programmers.co.kr/learn/courses/30/lessons/120956?language=python3
def solution(babbling):
    answer = 0
    for word in babbling:
        stack = ""
        for i in word:
            stack += i
            if(len(stack) == 2 and stack in ("ye", "ma")) or (len(stack) == 3 and stack in ("aya", "woo")):
                stack = ""
        if not stack:
            answer += 1
    return answer
