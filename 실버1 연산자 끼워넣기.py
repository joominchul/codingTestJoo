# https://www.acmicpc.net/problem/14888
def cal(op, num, depth):    # 계산하기
    if op == 0:
        num += seq[depth]
    elif op == 1:
        num -= seq[depth]
    elif op == 2:
        num *= seq[depth]
    else:
        if num > 0:
            num //= seq[depth]
        else:  # 음수의 절대값을 나눈 다음 - 부호를 붙임.
            num = (abs(num) // seq[depth]) * -1
    return num


def dfs(depth, result):
    global maxResult
    global minResult
    global opNum
    if depth == n:
        maxResult = max(maxResult, result)
        minResult = min(minResult, result)
    else:
        for i in range(4):
            if opNum[i] > 0:    # 연산자 티오가 있으면
                opNum[i] -= 1   # 티오를 하나 줄이고 재귀 호출
                dfs(depth + 1, cal(i, result, depth))
                opNum[i] += 1   # 티오 복구


n = int(input())
seq = list(map(int, input().split()))
opNum = list(map(int, input().split()))  # 여러 숫자 리스트로 입력 받기
maxResult = -1000000000
minResult = 1000000000
dfs(1, seq[0])
print(maxResult)
print(minResult)
