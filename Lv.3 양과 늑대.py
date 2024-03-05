#https://school.programmers.co.kr/learn/courses/30/lessons/92343
from collections import defaultdict
max_sheep = 0

def dfs(graph, v, sheep, wolf, moves, info):
    global max_sheep

    sheep += info[v] ^ 1    #1과 같지 않으면 1, 같으면 0
    wolf += info[v]         #양이면 0이므로, 늑대일때만 증가함. 
    if sheep > wolf:        #백트래킹
        max_sheep = max(max_sheep, sheep)#양의 수 갱신
        for edge in graph[v]:
            moves.add(edge) #자식 노드들 moves에 추가

        for move in moves:  #moves에서 move를 뺀 집합을 가지고 재귀
            dfs(graph, move, sheep, wolf, moves-set([move]), info)

def solution(info, edges):
    #graph = {i:[] for i in range(len(info))}
    graph = defaultdict(list)       #연결 관계 저장할 딕셔너리
    for vertex, edge in edges:
        graph[vertex].append(edge)  #연결 관계 저장. 부모 키에 자식 벨류.

    dfs(graph, 0, 0, 0, set(), info)#깊이 우선 탐색
    return max_sheep
