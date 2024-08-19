#https://school.programmers.co.kr/learn/courses/30/lessons/60058
def make_right_string(u, v):        #올바른 괄호 문자열 만들기
    string = "(" + v + ")"          #빈 문자열에 (와 v, )를 붙임
    #u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙임
    for i in range(1, len(u) - 1):  
        if u[i] == '(':
            string += ')'
        else:
            string += '('
    return string
def Balanced_string_separation(w):  #균형잡힌 괄호 문자열 분리
    u = ""
    v = ""
    left_bracket = 0    #(
    right_bracket = 0   #)
    for i in range(len(w)):
        if w[i] == '(':
            left_bracket += 1
        else:
            right_bracket += 1
        u += w[i]
        if right_bracket == left_bracket:   #균형잡힌 문자열이 되면 나머지는 v로 분류
            v += w[i+1:]
            break
    if right_string_check(u):       #u가 올바른 괄호 문자열이라면 문자열 v에 대해 1단계부터 다시 수행
        return u + Balanced_string_separation(v)
    else:                           #u가 "올바른 괄호 문자열"이 아니라면
        if right_string_check(v):   #v가 올바른 괄호 문자열이라면
            return make_right_string(u, v)
        else:                       #v가 "올바른 괄호 문자열"이 아니라면
            return make_right_string(u, Balanced_string_separation(v))
def right_string_check(string):    #올바른 괄호인지 확인
    bracket = []
    for w in string:
        if w == '(':
            bracket.append(w)
        else:
            if len(bracket) == 0:
                return False
            bracket.pop()
    if len(bracket) == 0:
        return True
    else:
        return False
def solution(p):
    if right_string_check(p):
        return p
    else:
        return Balanced_string_separation(p)
     
