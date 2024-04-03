from collections import deque
def check_change(begin, word):#변환할 수 있는지 확인
    length = len(begin)
    check = 0
    for i in range(length):
        if begin[i] != word[i]:
            check+=1
        if check > 1:
            return False
    if check == 1:
        return True
def solution(begin, target, words):
    answer = 0
    dq=deque()
    dq.append(begin)
    dic = {begin:0}
    while dq:   #큐가 있을 동안
        begin = dq.popleft()
        begin_num = dic.get(begin)
        if begin == target:
            answer = begin_num
            break
        for word in words:
                #word가 변환 가능하고 딕셔너리에 없다면
            if check_change(begin, word) and word not in dic:
                dic[word] = begin_num+1
                dq.append(word)
    return answer
