#https://school.programmers.co.kr/learn/courses/30/lessons/68936
zero = 0    #0의 개수
one = 0     #1의 개수
#압축할 수 있는지 확인. 
def checkZip(arr, x, y, n): #(배열, 영역 x좌표, 영역 y좌표, 영역 크기)
    standard = arr[x][y]    #영역 기준
    for i in range(n):
        for j in range(n):  #영역 기준과 다르면 2를 리턴
            if standard != arr[x + i][y + j]:
                return 2
    return standard         #같으면 기준 리턴
#배열의 0과 1 개수 카운트.
def zipArr(arr, x, y, n):   #(배열, 영역 x좌표, 영역 y좌표, 영역 크기)
    global zero
    global one
    if n == 1:              #영역이 1일 때, 개수 추가
        if arr[x][y] == 0:
            zero +=1
        else:
            one +=1
        return
                            #영역 압축 가능 체크
    result = checkZip(arr, x, y, n)
    if result != 2:         #압축 가능하면 개수 추가
        if result == 0:
            zero +=1
        else:
            one +=1
        return
    else:                   #압축 불가능하면 영역을 4등분 해서 재귀
        n = n//2            #n/2를 하면 실수 처리 돼서 오류남.
        zipArr(arr, x, y, n)
        zipArr(arr, x + n, y, n)
        zipArr(arr, x, y + n, n)
        zipArr(arr, x + n, y + n, n)
def solution(arr):
    global zero
    global one
    n = len(arr)
    zipArr(arr, 0, 0, n)    #배열의 0과 1 개수 카운트.
    return [zero, one]
