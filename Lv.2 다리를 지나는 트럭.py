#https://school.programmers.co.kr/learn/courses/30/lessons/42583
def solution(bridge_length, weight, truck_weights):
    answer = 0
    in_bridge = []
    in_bridge_sum = 0
    while(True):
        answer += 1
        #다리에 트럭 제거
        if(len(in_bridge) > 0 and (answer - in_bridge[0][1]) == bridge_length):
            temp = in_bridge.pop(0)
            in_bridge_sum -= temp[0]
        #다리에 트럭 추가
        if(len(truck_weights) > 0 and in_bridge_sum + truck_weights[0] <= weight):
            in_bridge.append([truck_weights[0], answer])
            in_bridge_sum += truck_weights.pop(0)
        if(len(truck_weights) == 0 and len(in_bridge) == 0):
            break
    return answer
