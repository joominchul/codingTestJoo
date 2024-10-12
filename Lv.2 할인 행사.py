#https://school.programmers.co.kr/learn/courses/30/lessons/131127
def solution(want, number, discount):
    answer = 0
    discount_dict = {}
    #각 물품 별 원하는 개수를 딕셔너리로 만듬
    for i in range(len(want)):
        discount_dict[want[i]] = number[i]
    #완전 탐색
    for start in range(len(discount) - 9):
        #10일 동안 물품 별 할인 날짜 개수 딕셔너리를 만듬.
        dic = {}
        for s in range(start, start + 10):
            temp = dic.get(discount[s])
            if temp:
                dic[discount[s]] = temp + 1
            else:
                dic[discount[s]] = 1
        #만든 딕셔너리와 기존 딕셔너리를 비교
        if discount_dict == dic:
            answer += 1
    return answer
