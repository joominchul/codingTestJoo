#https://school.programmers.co.kr/learn/courses/30/lessons/42576
def solution(participant, completion):
    pdict = {}
    for p in participant:
        temp = pdict.get(p)
        if temp:
            pdict[p] += 1
        else:
            pdict[p] = 1
    for c in completion:
        pdict[c] -= 1
    for p in pdict:
        if pdict[p] == 1:
            return p
