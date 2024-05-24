#https://school.programmers.co.kr/learn/courses/30/lessons/67257?language=python3
# 주어진 피연산자에 맞게 수식을 연산 후 그 결과값을 리턴
def cal(expression, operand):
    result = int(expression[0])
    for idx in range(1,len(expression)):
        if(operand == "*"):
            result*=int(expression[idx])
        elif(operand == "+"):
            result+=int(expression[idx])
        else:
            result-=int(expression[idx])
    return result
# 주어진 우선 순위에 따라 연산식을 계산 후 결과값을 리턴
def expressionCal(expression, operand):
    resultList = []     #임시 결과 리스트
    lowOp = operand[0]  #가장 낮은 우선 순위
    midOp = operand[1]  #중간 우선 순위
    hiOp = operand[2]   #가장 높은 우선 순위
    lowE = expression.split(lowOp)          #가장 낮은 우선 순위 피연산자로 연산식 분리
    for exp in lowE:                        #분리한 연산식을 가지고
        midE = exp.split(midOp)             #중간 우선 순위 피연산자로 분리
        tempList = []   #임시 리스트
        for exp in midE:                    #2번 분리한 연산식을 가지고
            hiE = exp.split(hiOp)           #가장 높은 우선 순위 피연산자로 분리
            tempList.append(cal(hiE,hiOp))  #분리한 숫자들을 가장 높은 우선 순위 피연산자로 계산 후 임시 리스트에 추가
        resultList.append(cal(tempList, midOp))#임시 리스트와 중간 순위 피연산자를 가지고 계산 후 임시 결과 리스트에 추가
    return cal(resultList,lowOp)            #임시 결과 리스트와 가장 낮은 순위 피연산자를 가지고 계산 후 값 리턴
def solution(expression):
    #우선 순위 피연산자 조합 리스트
    operandList = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
    answer = 0
    #피연산자 조합을 가지고
    for operand in operandList:
        #계산 결과를 절대값 처리한 다음에 기존 정답과 비교해 더 큰 값을 정답에 저장
        answer = max(answer, abs(expressionCal(expression, operand)))
    return answer
