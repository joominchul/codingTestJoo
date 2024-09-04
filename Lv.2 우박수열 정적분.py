#https://school.programmers.co.kr/learn/courses/30/lessons/134239
def solution(k, ranges):
    answer = []
    hail = [k]
    while k > 1:            #우박수열 만들기
        if(k%2 == 0):
            k //= 2
        else:
            k = k * 3 + 1
        hail.append(k)
    end = len(hail) - 1
    for ran in ranges:
        a = ran[0]
        b = ran[1]
        if b <= 0:           #b가 마이너스, 0일 경우
            b = end + b
        if a > b:           #시작점이 끝점보다 커서 유효하지 않을 때
            answer.append(-1)
            continue
        else:
            area = 0        #넓이 구하기
            for i in range(a, b):
                high = max(hail[i], hail[i+1])
                low = min(hail[i], hail[i+1])
                area += low + ((high - low) / 2)
            answer.append(area)
    return answer
