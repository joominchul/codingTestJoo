#https://school.programmers.co.kr/learn/courses/30/lessons/1844#
from collections import deque

def solution(maps):
    # 맵 크기
    n, m = len(maps), len(maps[0])
    
    # 방향 정의 (상, 하, 좌, 우)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    # 방문 여부 확인
    visited = [[False] * m for _ in range(n)]
    
    # BFS 큐 초기화 (x, y, 거리)
    queue = deque([(0, 0, 1)])
    visited[0][0] = True
    
    # BFS 실행
    while queue:
        x, y, distance = queue.popleft()
        
        # 도착지점 도달
        if x == n - 1 and y == m - 1:
            return distance
        
        # 4방향 탐색
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # 유효 범위 내이고, 방문하지 않았으며, 길이 존재하는 경우
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] == 1:
                visited[nx][ny] = True  # 방문 처리
                queue.append((nx, ny, distance + 1))
    
    # 도달할 수 없는 경우
    return -1
