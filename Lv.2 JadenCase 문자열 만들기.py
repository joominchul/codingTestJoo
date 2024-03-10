def solution(s):
    #공백으로 분할
    original = s.split(" ")
    #문자들을 모두 소문자로 바꾸는데, 공백이 연속일 경우 확실하게 공백으로 바꿈. 
    original = [" " if i =="" else i.lower() for i in original]
    change = ""
    #마지막 단어를 제외한 단어들을 JadenCase로 바꿈.
    for i in range(len(original)-1):
        #공백 문자일 경우 그대로 더해줌. 
        if original[i][0] == " ":
            change += original[i]
        #첫 문자가 알파벳이면 대문자로 바꿔주고, 그 외 알파벳은 그대로 소문자로 추가.
        elif original[i][0].islower():
            change += original[i][0].upper() + original[i][1:] + " "
        #첫 문자가 숫자이면 그대로 추가.
        else:
            change += original[i] + " "
    #마지막 단어가 공백이면 그대로 정답 리턴
    if original[-1][0] == " ":
        return change
    #마지막 단어의 첫 문자가 알파벳이면 대문자로 바꿔주고, 그 외 알파벳은 그대로 소문자로 추가.
    if original[-1][0].islower():
        change += original[-1][0].upper() + original[-1][1:]
    #마지막 단어의 첫 문자가 숫자이면 그대로 추가.
    else:
        change += original[-1]
    return change
