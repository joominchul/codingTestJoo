#거리두기 확인
def check(li):
    for i in range(5):
        for j in range(5):
            if(li[i][j] == "P"):
                #오른쪽 확인
                if(j+1<5):
                    if(li[i][j+1] == "P"):
                        return False
                    if(li[i][j+1] != "X" and j+2<5):
                        #오오른쪽 확인
                        if(li[i][j+2] == "P"):
                            return False
                #아래쪽 확인
                if(i+1<5):
                    if(li[i+1][j] == "P"):
                        return False
                    if(li[i+1][j] != "X" and i+2<5):
                        #아아래쪽 확인
                        if(li[i+2][j] == "P"):
                            return False
                #오른쪽 아래 확인
                if(i+1<5 and j+1<5):
                    if(li[i+1][j+1] == "P" and (li[i+1][j] != "X" or li[i][j+1] != "X")):
                        return False
                #왼쪽 아래 확인
                if(i+1<5 and j-1>=0):
                    if(li[i+1][j-1] == "P" and (li[i+1][j] != "X" or li[i][j-1] != "X")):
                        return False
                    
    return True
def solution(places):
    answer = []
    for li in places:
        if(check(li)):
            answer.append(1)
        else:
            answer.append(0)
    
    return answer
