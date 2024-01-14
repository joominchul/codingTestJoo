#https://school.programmers.co.kr/learn/courses/30/lessons/42888
def solution(record):
    answer = []
    NickName = {}
    for i in range(len(record)-1,-1,-1): #뒤에서부터 시작해 
        chat = record[i].split(" ")
        if not NickName.get(chat[1]) and chat[0] != "Leave": 
            #최종 닉네임을 NickName 딕셔너리에 아이디 별로 저장
            NickName.update({chat[1]:chat[2]})
    for i in record:
        chat = i.split(" ")
        if chat[0] == "Enter":
            #NickName 딕셔너리에서 아이디에 맞는 최종 닉네임으로 채팅 입력
            word = NickName[chat[1]] + "님이 들어왔습니다."
            answer.append(word)
        elif chat[0] == "Leave":
            word = NickName[chat[1]] + "님이 나갔습니다."
            answer.append(word)
    
    return answer
