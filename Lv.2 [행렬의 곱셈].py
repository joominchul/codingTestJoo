#https://school.programmers.co.kr/learn/courses/30/lessons/12949
def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)): #arr1의 행 개수만큼 반복
        tempList = [] #임시 행 리스트
        for j in range(len(arr2[0])): #행의 열을 채움, arr2의 열 길이만큼 반복
            temp = 0 #임시 값
            for k in range(len(arr1[0])): #행렬 곱함
                temp += (arr1[i][k] * arr2[k][j])
            tempList.append(temp)
        answer.append(tempList)
    return answer
