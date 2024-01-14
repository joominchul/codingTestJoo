#https://school.programmers.co.kr/learn/courses/30/lessons/161990
def solution(wallpaper):
    #lux, luy의 최소값, rdx, rdy의 최대값을 구한다. 
    
    #각 lux, luy의 최대 설정값, rdx, rdy의 최소 설정값
    lux = 50
    luy = 50
    rdx = 0
    rdy = 0
    for x in range(len(wallpaper)):
        for y in range(len(wallpaper[0])):
            if wallpaper[x][y] == '#':
                #값이 '#'일 때 x, y값과 lux, rdx, luy, rdy값을 비교해 변경
                if lux > x:
                    lux = x
                if luy > y:
                    luy = y
                if rdx < x:
                    rdx = x
                if rdy < y:
                    rdy = y
    # '#'파일을 완전히 드래그해야 함으로 rdx, rdy에 +1을 해준다. 
    answer = [lux, luy, rdx+1, rdy+1]
    return answer
