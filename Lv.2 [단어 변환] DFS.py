#https://school.programmers.co.kr/learn/courses/30/lessons/43163#
answer = [51] #변환할 수 없는 경우. 변환할 수 있는 최댓값이 50임.
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

def DFS(begin, target, words, num):
    global answer
    if begin == target: #변환이 완료되면 answer에 횟수 추가
        answer.append(num)
        return
    else:
        for idx, w in enumerate(words):
            if check_change(begin, w):  #변환이 가능하면 변환할 단어를 제외한 단어 리스트로 DFS
                else_words = words[:idx] + words[idx+1:]    #변환할 단어를 제외한 단어 리스트
                DFS(w, target, else_words, num+1)
    
def solution(begin, target, words):
    num=0
    DFS(begin, target, words, num)
    if min(answer) == 51:   #변환할 수 없는 경우 0 리턴
        return 0
    return min(answer)
