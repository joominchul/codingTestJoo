#https://school.programmers.co.kr/learn/courses/30/lessons/12911
#이진수의 1의 개수 리턴하는 함수
def findOne(nBin):
    one = 0
    for n in nBin:
        if n == "1":
            one += 1
    return one
def solution(n):
    answer = n
    nBin = bin(n)[2:]
    nOne = findOne(nBin)
    while(True):
        answer += 1
        answerBin = bin(answer)[2:]
        answerOne = findOne(answerBin)
        if nOne == answerOne:
            break
    return answer
