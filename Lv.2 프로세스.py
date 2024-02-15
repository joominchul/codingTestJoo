#https://school.programmers.co.kr/learn/courses/30/lessons/42587
def que(priorities):                    #priorities 리스트를 [우선순위, 대기 순서]로 바꿈
    que = []
    num=0
    for i in priorities:
        que.append([i, num])
        num+=1
    return que

def solution(priorities, location):
    process = que(priorities)           #바꾼 실행 대기 큐
    answer = 0
    while True:
        priority = max(process)[0]      #실행 대기 큐에서 가장 높은 우선순위
        now_process = process.pop(0)    #순서 1.
        if now_process[0] < priority:   #순서 2.
            process.append(now_process)
        else:                           #순서 3.
            answer+=1                   #실행 순서 +1
            if now_process[1] == location:#실행된 프로세스가 알고 싶은 프로세스일 때
                return answer
        
    
