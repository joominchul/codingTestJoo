#https://school.programmers.co.kr/learn/courses/30/lessons/76502
def solution(s):
    answer = 0
    for i in range(len(s)):
        stack = []
        right = False
        count = 0
        for j in range(i, len(s)):
            count += 1
            if s[j] == "[" or s[j] == "{" or s[j] == "(":
                stack.append(s[j])
            else:
                if stack:
                    w = stack.pop()
                    if (w == "[" and s[j] == "]") or (w == "{" and s[j] == "}") or (w == "(" and s[j] == ")"):
                        right = True
                    else:
                        right = False
                        break
                else:
                    right = False
                    break
        for j in range(i):
            count += 1
            if s[j] == "[" or s[j] == "{" or s[j] == "(":
                stack.append(s[j])
            else:
                if stack:
                    w = stack.pop()
                    if (w == "[" and s[j] == "]") or (w == "{" and s[j] == "}") or (w == "(" and s[j] == ")"):
                        right = True
                    else:
                        right = False
                        break
                else:
                    right = False
                    break
        if right and not stack and count == len(s):
            answer += 1
                
    return answer
