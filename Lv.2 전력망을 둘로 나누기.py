#https://school.programmers.co.kr/learn/courses/30/lessons/86971
def find_connected_component(graph) :   #전력망의 송전탑 개수 차이 리턴
    visited = set()					    #방문한 송전탑 저장
    num=[]                              #전력망 별 송전탑 개수 리스트
    for top in graph :                  #키(송전탑) 별
        if top not in visited :		    #만약 키(송전탑)을 방문하지 않았다면
            elec = dfs_cc(graph, [], top, visited)#전력망을 구축하고
            num.append(len(elec))	    #전력망의 송전탑 개수를 num에 추가
    return abs(num[0]-num[1])           #송전탑 개수 차이 절대값 리턴

def dfs_cc(graph, elec, top, visited):  #전력망 구축
    if top not in visited :             #송전탑에 방문 안 했으면    
        visited.add(top)				#방문 송전탑 집합에 추가
        elec.append(top)			    #전력망 리스트에 송전탑 추가
        nbr = graph[top] - visited		#송전탑과 연결된 송전탑 중 방문하지 않은 송전탑들
        for t in nbr:					#이웃 송전탑들 방문
            dfs_cc(graph, elec, t, visited)
    return elec	
def makeTree(wires):                    #wires를 딕셔너리 형태로 변환
    tree = {}                           #트리 딕셔너리
    for wire in wires:
        if tree.get(wire[0]):           #v1이 딕셔너리에 키로 있으면
            temp = tree.get(wire[0])    
            temp.add(wire[1])
            tree[wire[0]] = temp        #v2를 v1의 값으로 추가
        if not tree.get(wire[0]):       #v1이 딕셔너리에 키로 없으면 업데이트
            tree.update({wire[0]: set([wire[1]])})
        if tree.get(wire[1]):           #v2가 딕셔너리에 키로 있으면
            temp = tree.get(wire[1])
            temp.add(wire[0])
            tree[wire[1]] = temp        #v1을 v2의 값으로 추가
        if not tree.get(wire[1]):       #v2가 딕셔너리에 키로 없으면 업데이트
            tree.update({wire[1]: set([wire[0]])})
    return tree
            
def solution(n, wires):
    tree = makeTree(wires)              #wires를 딕셔너리 구조로 변환
    answer = n                          #정답
    for wire in wires:                  #각 전선들을 하나씩 끊어봄
        tree.get(wire[0]).remove(wire[1])#트리에서 전선을 끊음
        tree.get(wire[1]).remove(wire[0])
        answer = min(answer, find_connected_component(tree))#송전탑의 개수 차가 작은 걸 정답으로 변경
        tree.get(wire[0]).add(wire[1])  #끊은 전선을 원상복구 시킴
        tree.get(wire[1]).add(wire[0])
    return answer
