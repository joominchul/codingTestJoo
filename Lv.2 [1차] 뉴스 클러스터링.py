#https://school.programmers.co.kr/learn/courses/30/lessons/17677
def changeWord(word):
    if word.isalpha():
        return word.lower()
    else:
        return ''
    
def solution(str1, str2):
    intersection = 0
    str1_list = []
    str2_list = []
    #str1 다중 집합
    for i in range(len(str1) - 1):
        s1 = changeWord(str1[i])
        s2 = changeWord(str1[i + 1])
        if s1 != '' and s2 != '':
            str1_list.append(s1 + s2)
    #str2 다중 집합
    for i in range(len(str2) - 1):
        s1 = changeWord(str2[i])
        s2 = changeWord(str2[i + 1])
        if s1 != '' and s2 != '':
            str2_list.append(s1 + s2)
    s1_len = len(str1_list)
    s2_len = len(str2_list)
    if(s1_len == 0 and s2_len == 0):
        return 65536
    for i in range(s1_len):
        for j in range(s2_len - intersection):
            if(str1_list[i - intersection] == str2_list[j]):
                str1_list.pop(i - intersection)
                str2_list.pop(j)
                intersection += 1
                break
    union = len(str1_list) + len(str2_list) + intersection
    return (intersection / union) * 65536 // 1
