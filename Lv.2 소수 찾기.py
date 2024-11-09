from itertools import permutations
def checkSosu(num):
    #2, 3은 검사 못 함
    for i in range(2, num//2+1):
        if(num%i) == 0:
            return False
    return True
def addAnswer(n):
    add = 0
    if n == 2 or n == 3:
        add = 1
    elif n <= 1:
        add = 0
    else:
        if checkSosu(n):
            add = 1
    return add
def solution(numbers):
    answer = 0
    length = len(numbers)
    numberSet = set()
    while length > 0:
        #길이 별 순열 구함
        for li in list(permutations(numbers, length)):
            number = ""
            for num in li:
                number += num
            n = int(number)
            if n not in numberSet:
                answer += addAnswer(n)
                numberSet.add(n)
        length -= 1
    return answer
