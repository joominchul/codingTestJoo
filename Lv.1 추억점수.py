def solution(name, yearning, photo):
    answer = []
    NY = {}
    numN = len(name)
    
    for i in range(numN):
        NY[name[i]] = yearning[i]
        
    for i in range(len(photo)):
        numY=0
        for j in photo[i]:
            if(j in NY):
                numY+=NY[j]
        answer.append(numY)
        
    return answer
