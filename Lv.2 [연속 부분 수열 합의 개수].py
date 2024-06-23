#https://school.programmers.co.kr/learn/courses/30/lessons/131701
def sumList(elements, length, sumSet):  #길이가 2 이상인 부분 수열 합 구하는 함수.
    lenElements = len(elements)         #수열 길이
    temp = 0    #임시 값
    for i in range(lenElements):        #수열 탐색
        if(temp == 0):  #처음 부분 수열 합을 구할 경우
            for j in range(length):     #길이에 따라 더함
                temp += elements[i+j]
        else:           #합을 이미 구한 경우
            #print("temp ", temp, " - ", elements[i-1], " + ",elements[(i+length-1)%lenElements])
            #부분 수열 합에서 이전 값을 빼고 새로운 값을 더함.
            temp = temp - elements[i-1] + elements[(i+length-1)%lenElements]
        sumSet.add(temp)#집합에 합을 추가함.
        #print(sumSet)
def solution(elements):
    sumSet = set()
    for element in elements:            #길이가 1인 부분 집합 합을 집합에 추가
        sumSet.add(element)
    for i in range(2,len(elements)+1):  #길이가 2 이상인 부분 집합 합을 집합에 추가
        sumList(elements, i, sumSet)
    answer = len(sumSet)
    return answer
