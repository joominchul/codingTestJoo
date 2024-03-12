#https://school.programmers.co.kr/learn/courses/30/lessons/12909
def solution(s):
    #괄호를 저장할 스택
    stack = []      
    for w in s:
        #왼쪽 괄호이면 스택에 추가
        if w == "(":
            stack.append(w)
        #오른쪽 괄호일 때
        else:
            #스택이 비었으면 거짓
            if not stack:
                return False
            #스택이 있으면 하나 삭제
            stack.pop()
    #문자열을 다 돌았는데도 스택이 있으면 거짓
    if stack:
        return False
    #스택이 다 비었으면 참
    return True
