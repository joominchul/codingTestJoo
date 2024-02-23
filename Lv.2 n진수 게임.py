#https://school.programmers.co.kr/learn/courses/30/lessons/17687
alpha = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
def digit(n, num, li):              #n진수를 배열로 리턴
    li.append(num%n)
    if num<n:
        li.reverse()
        return li
    else:
        return digit(n, num//n, li)
    
def solution(n, t, m, p):
    answer = ""
    num = 0
    turn = 0
    while len(answer) < t:          #answer의 길이가 미리 구할 숫자보다 적을 동안
        temp = digit(n, num, [])    #temp에 숫자를 n진수로 변환한 배열을 저장
        for i in temp:
            if len(answer) == t:    #answer의 길이가 미리 구할 숫자와 같으면 종료
                break
            if (turn%m)+1 == p:     #자신의 차례가 되면
                turn+=1             #차례+1
                if i>=10:           #만약 숫자가 10이상이면
                    answer+=alpha[i]#알파벳 대문자를 answer에 추가
                else:               #10미만이면
                    answer += str(i)#str로 변환 후 추가
            else:                   #남의 차례이면
                turn+=1             #차례+1
        num+=1                      #진수를 다 확인했으면 숫자+1
    return answer
