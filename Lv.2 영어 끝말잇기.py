#https://school.programmers.co.kr/learn/courses/30/lessons/12981
def solution(n, words):
    history = {}    #나왔던 숫자들을 저장하는 딕셔너리
    count = 0       #끝말잇기 단어 수
    lastWord = ""   #직전 단어
    for w in words:
        #처음 시작 시
        if count == 0:
            #딕셔너리에 단어 추가
            history[w] = (count % n) + 1 #값은 별 의미 없음
            #단어 수를 추가해주고, 직전 단어에 단어 저장
            count += 1
            lastWord = w
        #끝말잇기가 이어지는 경우
        elif history.get(w) == None and lastWord[-1] == w[0]:
            history[w] = (count % n) + 1
            count += 1
            lastWord = w
        #끝말잇기가 실패하는 경우
        else:
            return [(count % n) + 1, (count // n) + 1]
    #실패하지 않은 경우
    return [0,0]
