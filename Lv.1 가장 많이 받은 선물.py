#https://school.programmers.co.kr/learn/courses/30/lessons/258712
def solution(friends, gifts):
    answer = 0
    friend_dict = {}
    friend_dict1 = {}
    friend_gift = {}
    friend_count = {}
    for f in range(len(friends)):   #프렌즈 순서, 선물 지수, 선물 받은 기록 설정
        friend_dict[friends[f]] = f
        friend_dict1[f] = friends[f]
        friend_count[friends[f]] = 0
        friend_gift[friends[f]] = [0] * len(friends)
    for gift in gifts:              #선물 주고받은 기록 설정
        send, recieve = gift.split(" ")
        friend_gift[send][friend_dict[recieve]] += 1
        friend_gift[recieve][friend_dict[send]] -= 1
        friend_count[send] += 1
        friend_count[recieve] -= 1
    for friend in friends:
        temp_answer = 0
        for i in range(len(friends)):
            gift_count = friend_gift[friend][i]
            if gift_count > 0:      #선물 주고받은 기록이 양수일 경우
                temp_answer += 1
            if gift_count == 0 and friend_count[friend] > friend_count[friend_dict1[i]]:
                temp_answer += 1    #기록이 없거나 수가 같을 경우 선물 지수가 더 큰 사람이 받
        answer = max(answer, temp_answer)    
    return answer
