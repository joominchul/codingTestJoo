#https://school.programmers.co.kr/learn/courses/30/lessons/43165
def Sum(numbers, i):                #계산 안한 나머지의 총 합
    s = 0
    for n in range(i, len(numbers)):
        s+=numbers[n]
    return s

def cul(numbers,i, target, temp):   #깊이 우선 탐색
    plus = temp + numbers[i]        #임시 값에 i번째 값을 더함
    minus = temp - numbers[i]       #임시 값에 i번째 값을 뺌
    if i == len(numbers)-1:         #다 돌았는데
        if plus == target or minus == target:
                                    #플러스나 마이너스 값이 타겟과 같으면 1
            return 1
        else:                       #아니면 0
            return 0
    else:                           #다 돌지 않았다면
        if (plus-Sum(numbers, i+1))>target and (minus+Sum(numbers, i+1))<target:
                                    #나머지를 다 더하거나 뺐을 때 타겟보다 작거나 크면
                                    #(타겟과 같아질 수 없으면)
            return 0
        elif (plus-Sum(numbers, i+1))>target:
                                    #나머지를 다 빼도 타겟보다 크면
            return cul(numbers,i+1, target, minus)
        elif (minus+Sum(numbers, i+1))<target:
                                    #나머지를 다 더해도 타겟보다 작으면
            return cul(numbers,i+1, target, plus)
        else:                       #플러스와 마이너스인 경우를 재귀 호출
            return cul(numbers,i+1, target, minus) + cul(numbers,i+1, target, plus)
        
def solution(numbers, target):
    numbers.sort(reverse=True)      #역순으로 정렬
    answer = cul(numbers,0, target, 0)
    return answer
