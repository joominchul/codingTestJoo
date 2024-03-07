#https://school.programmers.co.kr/learn/courses/30/lessons/12939
def solution(s):
    #공백으로 구분
    s_list = s.split(" ")
    #문자열을 정수로 변환
    s_list = [int(i) for i in s_list]
    #정답 선언
    answer = ""
    #정수 리스트의 최솟값과 최대값을 문자열로 변환
    answer = str(min(s_list)) + " " + str(max(s_list))
    return answer
