directions = {
      'E': [0, 1],
      'W': [0, -1],
      'S': [1, 0],
      'N': [-1, 0],
    }
def findS(park):
    for yI, y in enumerate(park):
        if("S" in y):
            return [yI, y.index("S")]

def go(start, park, i):
    move=int(i[2])
    x_plus, y_plus = directions[i[0]]
    temp = start.copy()
    for i in range(move):
        temp[0]+=x_plus
        temp[1]+=y_plus
        if((temp[0]<len(park))and(temp[0]>=0)and(temp[1]<len(park[0]))and(temp[1]>=0))!=True:
            return start
        if(park[temp[0]][temp[1]]=="X"):
            return start
    return temp
        
def solution(park, routes): 
    
    start = findS(park)
    for i in routes:
        start=go(start, park, i)
    return start
