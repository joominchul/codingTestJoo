#https://school.programmers.co.kr/learn/courses/30/lessons/49994
def solution(dirs):
    answer = 0
    now = [0,0]
    visited = []
    
    for direct in dirs:
        if direct == "U" and now[1] <= 4:
            #이동한 위치
            temp = (now[0], now[1] + 1)
            #집합에 출발 좌표와 도착 좌표를 추가함.
            go = set()
            #튜플은 변경할 수 없는 원소이므로 집합의 원소로 사용 가능.
            go.add(tuple(now.copy()))
            go.add(temp)
            now[1] += 1
            if go not in visited:
                visited.append(go)
                
        if direct == "D" and now[1] >= -4:
            temp = (now[0], now[1] - 1)
            go = set()
            go.add(tuple(now.copy()))
            go.add(temp)
            now[1] -= 1
            if go not in visited:
                visited.append(go)
                
        if direct == "R" and now[0] <= 4:
            temp = (now[0] + 1, now[1])
            go = set()
            go.add(tuple(now.copy()))
            go.add(temp)
            now[0] += 1
            if go not in visited:
                visited.append(go)
                
        if direct == "L" and now[0] >= -4:
            temp = (now[0] - 1, now[1])
            go = set()
            go.add(tuple(now.copy()))
            go.add(temp)
            now[0] -= 1
            if go not in visited:
                visited.append(go)
    return len(visited)
