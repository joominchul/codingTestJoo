#https://school.programmers.co.kr/learn/courses/30/lessons/70129?language=python3
def solution(s):
    answer = []
    count = 0
    deletedZero = 0
    while(s != "1"):
        sLen = len(s)
        zero = 0
        for i in s:
            if(i=="0"):
                zero +=1
        s = bin(sLen-zero)[2:]
        count += 1
        deletedZero += zero
    return [count, deletedZero]
