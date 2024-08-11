# https://www.acmicpc.net/problem/14888
def cal(order):
    result = seq[0]
    for i in range(1, n):  # order의 숫자에 따라 계산을 함
        if order[i - 1] == "0":
            result += seq[i]
        elif order[i - 1] == "1":
            result -= seq[i]
        elif order[i - 1] == "2":
            result *= seq[i]
        else:
            if result > 0:
                result //= seq[i]
            else:  # 음수의 절대값을 나눈 다음 - 부호를 붙임.
                result = (abs(result) // seq[i]) * -1
    return result


def dfs(depth, order):
    global maxResult
    global minResult
    global opNum
    if depth == 0:
        result = cal(order)  # 연산에 따라 계산
        maxResult = max(maxResult, result)
        minResult = min(minResult, result)
    else:
        for i in range(4):
            if opNum[i] > 0:    # 연산자 티오가 있으면
                opNum[i] -= 1   # 티오를 하나 줄이고 재귀 호출
                dfs(depth - 1, order + str(i))
                opNum[i] += 1   # 티오 복구


n = int(input())
seq = list(map(int, input().split()))
opNum = list(map(int, input().split()))  # 여러 숫자 리스트로 입력 받기
maxResult = -1000000000
minResult = 1000000000
dfs(n - 1, "")
print(maxResult)
print(minResult)
