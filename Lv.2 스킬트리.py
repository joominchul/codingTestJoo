#https://school.programmers.co.kr/learn/courses/30/lessons/49993?language=python3
def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        skill_list = list(skill)            #스킬 순서를 리스트로 변환해 저장
        for s in tree:
            if s in skill:                  #만약 스킬이 스킬 순서에 있는데,
                if s != skill_list.pop(0):  #스킬 순서의 첫번째가 아니라면 건너뜀
                    break
        else:                               #for문을 다 돌았다면 스킬 트리 가능
            answer += 1
    return answer
