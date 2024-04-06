#https://school.programmers.co.kr/learn/courses/30/lessons/42586
def solution(progresses, speeds):
    answer = []
    #남은 기능이 있을 때까지 반복
    while len(progresses) > 0:
        release = True  #배포 가능한지
        n = 0           #배포한 기능 수
        #남은 기능들
        for i in range(len(progresses)):
            #기능 진도율 업데이트
            progresses[i-n] += speeds[i-n]
            #진도율이 100%가 넘었고, 배포 가능할 때
            if progresses[i-n] >=100 and release:
                #progresses와 speeds에서 기능 제거 -> 배포
                progresses.pop(i-n)
                speeds.pop(i-n)
                #배포한 기능 수 +1
                n+=1
            #배포 불가능하면
            else:
                release = False
        #배포한 기능이 있으면
        if n > 0:
            answer.append(n)
    return answer
