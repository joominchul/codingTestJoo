#https://school.programmers.co.kr/learn/courses/30/lessons/258711
def putEdge(Dict, key, value): #딕셔너리에 엣지 추가
    if Dict.get(key): #키가 딕셔너리에 있으면 값을 추가
        temp = Dict.get(key)
        temp.append(value)
        Dict[key] = temp
    else: #키가 딕셔너리에 없으면 업데이트
        Dict.update({key: [value]})
def inAout(edges):
    In = {} #입력 딕셔너리. 키 엣지에 입력으로 들어오는 엣지를 값으로 설정
    Out = {} #출력 딕셔너리. 키 엣지에서 출력으로 내보내는 엣지를 값으로 설정
    Max = 0 #엣지의 개수 변수
    for i in edges:
        putEdge(In, i[1], i[0])
        putEdge(Out, i[0], i[1])
        if Max <max(i): #엣지 개수 업데이트
            Max = max(i)
    return In, Out, Max
    
def solution(edges):
    In = {}
    Out = {}
    In, Out, Max = inAout(edges)
    answer = [0,0,0,0]
    for i in range(1,Max+1): #엣지 개수만큼 for문
        if Out.get(i): #i엣지의 출력이 있으면
            if In.get(i): #i엣지의 입력이 있으면
                #i엣지의 입력과 출력이 모두 2 이상이면
                #8자형 그래프
                if len(In.get(i))>1 and len(Out.get(i))>1:
                    answer[3]+=1
            else:
                #i엣지의 입력이 없고, 출력의 숫자가 2 이상이면
                #생성 정점
                if len(Out.get(i))>1:
                    answer[0] = i
        else:
            #i엣지의 출력이 없으면
            #막대형 그래프
            answer[2]+=1
    # 도넛형 그래프 수 = 생성 정점의 출력수 - 막대형 그래프 수 - 8자형 그래프 수
    answer[1] = len(Out.get(answer[0]))-answer[2]-answer[3]
    return answer
    
