#https://school.programmers.co.kr/learn/courses/30/lessons/64065
def solution(s):
    answer = []
    Set = {}            #집합 길이를 키로, 집합 원소들을 값으로 하는 딕셔너리
    templist = []       #임시 리스트
    tempstr = ""        #임시 원소
    checkset = False    #집합 시작 판단
    #문자열을 가지고 딕셔너리를 구성함.
    for i in range(1, len(s)-1):
        #집합이 끝날 때,
        if s[i] == "}":
            #원소가 1개만 있는 경우 임시 리스트에 원소 추가
            if tempstr != "":
                templist.append(tempstr)
                tempstr = ""
            #딕셔너리에 추가
            Set[len(templist)] = templist
            #집합 끝
            checkset = False
        #집합이 시작될 때, 임시 리스트를 초기화 하고, 집합 시작
        elif s[i] == "{":
            templist = []
            checkset = True
        elif s[i] == ",":
            #집합이 아직 안 끝났으면 임시 원소를 임시 리스트에 추가하고 임시 원소 초기화
            if checkset:
                templist.append(tempstr)
                tempstr = ""
            #집합이 끝났으면 아무 일 없음.
        #숫자를 임시 원소에 더함
        else:
            tempstr += s[i]
    #정답에 원소 추가. 1~가장 긴 집합의 길이
    for i in range(1,max(Set.keys())+1):
        temp = Set[i]
        for j in temp:
            j = int(j)
            #집합의 원소가 정답에 없으면 정답 리스트에 추가
            if j not in answer:
                answer.append(j)
                break
    return answer
