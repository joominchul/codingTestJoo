#https://school.programmers.co.kr/learn/courses/30/lessons/42578
def solution(clothes):
    answer = 1
    cloth_dict = {}
    #종류별 딕셔너리 생성
    for cloth in clothes:
        temp = cloth_dict.get(cloth[1])
        if temp:
            cloth_dict[cloth[1]] += 1
        else:
            cloth_dict[cloth[1]] = 2
    
    for k in cloth_dict:
        answer *= cloth_dict[k]
    return answer - 1
