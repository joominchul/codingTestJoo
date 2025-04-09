from collections import defaultdict
from collections import deque

n, m, v = input().split(" ") #입력 값 받기
graph = defaultdict(list)
for i in range(int(m)):
    v1, v2 = input().split(" ")  #간선이 연결하는 두 정점 받기
    graph[int(v1)].append(int(v2))
    graph[int(v2)].append(int(v1))  #양방향
answer1 = []    #dfs 답
answer2 = []    #bfs 답
for i in graph:
    graph[i].sort() #정점이 작은 것부터 방문하도록 정렬
def dfs(v):    #방문할 노드와 방문한 노드들 
    answer1.append(v)

    for i in graph[v]:
        if i not in answer1:
            dfs(i)
def bfs(v):
    que = deque()
    que.append(v)
    answer2.append(v)
    while(que):
        node = que.popleft()
        for i in graph[node]:
            if i not in answer2:
                answer2.append(i)
                que.append(i)
dfs(int(v))
bfs(int(v))

result = ' '.join(str(x) for x in answer1)
print(result)
result = ' '.join(str(x) for x in answer2)
print(result)
