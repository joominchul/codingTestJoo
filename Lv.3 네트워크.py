#https://school.programmers.co.kr/learn/courses/30/lessons/43162
def bfs(computers, visited, start):
        stack = [start]
        while stack:
            s = stack.pop()
            if visited[s] == 0: #방문 안 한 곳이라면
                visited[s] = 1
            for i in range(0, len(computers)):
                if computers[s][i] ==1 and visited[i] == 0: #연결 되어 있는데 방문 안 한 곳이라면
                    stack.append(i)     #스택에 추
def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]
    i=0
    while 0 in visited:                 #방문 안 한 곳이 있다면
        if visited[i] ==0:
            bfs(computers, visited, i)
            answer +=1
        i+=1
    return answer
