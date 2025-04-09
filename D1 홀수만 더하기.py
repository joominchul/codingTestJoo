#https://swexpertacademy.com/main/solvingProblem/solvingProblem.do
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
answer = ""
for test_case in range(1, T + 1):
    temp_answer = "#" + str(test_case) + " "
    int_answer = 0
    #10개의 수 입력 받기
    n1, n2, n3, n4, n5, n6, n7, n8, n9, n10 = map(int, input().split())
    if n1 % 2 != 0:
        int_answer += n1
    if n2 % 2 != 0:
        int_answer += n2
    if n3 % 2 != 0:
        int_answer += n3
    if n4 % 2 != 0:
        int_answer += n4
    if n5 % 2 != 0:
        int_answer += n5
    if n6 % 2 != 0:
        int_answer += n6
    if n7 % 2 != 0:
        int_answer += n7
    if n8 % 2 != 0:
        int_answer += n8
    if n9 % 2 != 0:
        int_answer += n9
    if n10 % 2 != 0:
        int_answer += n10
    temp_answer += str(int_answer)
    answer += temp_answer + "\n"
print(answer)
