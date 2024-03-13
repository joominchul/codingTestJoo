#https://school.programmers.co.kr/learn/courses/30/lessons/92341
#올림 나누기
def div(num, n):
    #초과한 시간이 단위 시간으로 나누어 떨어지면 그대로 나누기
    if num%n==0:
        return num/n
    #나누어 떨어지지 않으면 올림
    else:
        return (num//n)+1
#누적 주차 시간 계산
def calTime(time):
    num = len(time)
    #입차 후 출차 내역이 없다면 23:59에 출차한 것으로 간주
    if num % 2 != 0:
        time.append("23:59")
    #입출차 기록을 분 단위로 바꾸어 int_time에 저장
    int_time = []
    for t in time:
        t = int(t[0:2]) * 60 + int(t[3:])
        int_time.append(t)
    total = 0
    In = 0
    Out = 0
    for i in range(len(time)):
        #짝수 번째 기록이면 입차 기록, 홀수 번째 기록이면 출차 기록. 
        if i % 2 == 0:
            In = int_time[i]
        else:
            Out = int_time[i]
            #출차 시간에서 입차 시간을 빼 total에 저장
            total += (Out - In)
    return total
#주차 요금 계산
def calFee(fees, time):
    #요금표 정의
    default_time = fees[0]
    default_fee = fees[1]
    unit_time = fees[2]
    unit_fee = fees[3]
    #누적 주차 시간이 기본 시간 이하라면 기본 요금 청구
    if time <= default_time:
        return default_fee
    #초과하면 기본 요금 + 초과한 시간에 대해서 단위 시간마다 단위 요금 청구
    else:
        return default_fee + (div(time - default_time, unit_time) * unit_fee)
def solution(fees, records):
    answer = []
    #각 차량에 대한 주차 기록 딕셔너리 생성
    park = {}
    for r in records:
        #공백으로 시각, 차량번호, 내역을 구분
        temp = r.split(" ")
        #차량에 대한 시각 정보가 있었으면 추가, 없었으면 새로 생성
        car_time = park.get(temp[1])
        if car_time:
            car_time.append(temp[0])
            park[temp[1]] = car_time
        else:
            park.update({temp[1] : [temp[0]]})
    #각 차량에 대해
    for car in park:
        time = park.get(car)
        #누적 주차 시간을 구함
        total_time = calTime(time)
        #그에 따른 차량 주차 요금을 구함
        fee = calFee(fees, total_time)
        #answer 리스트에 차량과 요금을 추가함.
        answer.append([car, fee])
    #차량 번호에 따라 오름차순
    answer.sort()
    #주차 요금을 차량 번호가 작은 순서대로 담음.
    answer = [i[1] for i in answer]
    return answer
