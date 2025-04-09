#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AZVqPrHaAy_HBIOy&categoryId=AZVqPrHaAy_HBIOy&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
answer = ""
for test_case in range(1, T + 1):
    L_max = 0   #?를 L로 했을 때 최대값
    R_max = 0   #?를 R로 했을 때 최대값
    L_now = 0   #?를 L로 했을 때 현재 로봇 위치
    R_now = 0   #?를 R로 했을 때 현재 로봇 위치
    order = input() #명령어 입력 받음
    for s in order:
        if s == "L":
            L_now -= 1
            R_now -= 1
        if s == "R":
            L_now += 1
            R_now += 1
        if s == "?":   #?일 경우 ?를 L로 했다 가정하거나 R로 했다 가정함
            L_now -= 1
            R_now += 1
        #최대 거리 동기화
        L_max = max(L_max, abs(L_now))
        R_max = max(R_max, abs(R_now))
    answer += str(max(L_max, R_max)) + "\n"
print(answer)
