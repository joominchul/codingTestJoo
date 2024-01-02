import sys
sys.setrecursionlimit(10000) #재귀 깊이 설정
def updateIsland(island, i, j): #island 딕셔너리에 방문한 땅 업데이트
    if not island.get(i): #i키에 내용이 없는 경우
        island.update({i:[j]})
        return island
    else :
        temp=island.get(i)
        temp.append(j)
        island[i]=temp
        return island
def sumFood(maps, x, y, island, sum): #재귀DFS
    sum+=int(maps[x][y]) #sum에 식량 숫자 추가
    island=updateIsland(island, x, y) #island 업데이트
    if x!=0 and maps[x-1][y] != 'X' and y not in island[x-1]: #상
        sum, island = sumFood(maps, x-1, y, island, sum)
    if x<(len(maps)-1) and maps[x+1][y] != 'X' and y not in island[x+1]: #하
        sum, island = sumFood(maps, x+1, y, island, sum)
    if y!=0 and maps[x][y-1] != 'X' and (y-1) not in island[x]: #좌
        sum, island = sumFood(maps, x, y-1, island, sum)
    if y<(len(maps[0])-1) and maps[x][y+1] != 'X' and (y+1) not in island[x]: #우
        #확인해 바다가 아니고 방문하지 않았으면 재귀호출
        sum, island = sumFood(maps, x, y+1, island, sum)
    return sum, island
def solution(maps):
    answer = []
    island={}
    sum=0
    MapsNum=len(maps)
    MapsINum=len(maps[0])
    for i in range(MapsNum): #island 딕셔너리 초기화
        island.update({i:[]})
    for i in range(MapsNum):
        for j in range(MapsINum):
            if maps[i][j] !='X' and j not in island[i]: #바다가 아니고 방문하지 않은 섬이면
                sum, island = sumFood(maps, i, j, island, sum)
                answer.append(sum)
                sum=0
    if not answer:
        return [-1]
    else:
        answer.sort()
        return answer