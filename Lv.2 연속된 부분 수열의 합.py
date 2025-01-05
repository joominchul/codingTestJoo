#https://school.programmers.co.kr/learn/courses/30/lessons/178870
from collections import deque 
def solution(sequence, k):
    answer = []
    que = deque()   #부분 수열
    sum_ = 0
    count = 1000001 #부분 수열의 최대 길이
    for i in range(len(sequence)):
        if(sequence[i] > k):    #원소의 값이 k보다 크다면 앞으로도 계속 클테니 더 볼 필요 없음.
            break
        if(sequence[i] == k):   #원소의 값이 k이면 이거보다 부분 수열의 길이가 짧을 수 없으니 바로 리턴해줌.
            return [i, i]
        else:
            sum_ += sequence[i] #부분 수열의 합에 원소 값 추가
            que.append(i)       #부분 수열에 원소 인덱스 추가
            while(sum_ > k):    #합이 k보다 크다면 작거나 같을 때가지 부분 수열의 맨 앞 원소를 제거
                sum_ -= sequence[que.popleft()]
            if(sum_ == k and count > len(que)): #부분 수열의 합이 k와 같고 부분 수열의 길이가 기존보다 짧은 경우
                answer = [que[0], que[-1]]      #정답과 수열의 길이를 갱신
                count = len(que)
    return answer
