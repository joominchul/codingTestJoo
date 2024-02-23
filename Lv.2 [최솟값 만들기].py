#https://school.programmers.co.kr/learn/courses/30/lessons/12941
def solution(A,B):
    answer = 0
    A.sort()                #A를 오름차순으로 정렬
    B.sort(reverse = True)  #B를 내림차순으로 정렬
    for i in range(len(A)):
        answer+=A[i]*B[i]   #순서대로 곱하고 더함
    return answer
