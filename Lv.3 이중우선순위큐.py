#https://school.programmers.co.kr/learn/courses/30/lessons/42628
def solution(operations):
    que = []
    for op in operations:
        operation, num = op.split(" ")
        if operation == "I":
            que.append(int(num))
        else:
            if num == "1":
                que.sort()
                if(que):
                    que.pop(-1)
            else:
                que.sort()
                if(que):
                    que.pop(0)
    if(que):
        return [max(que), min(que)]
    return [0,0]
