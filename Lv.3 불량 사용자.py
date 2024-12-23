#https://school.programmers.co.kr/learn/courses/30/lessons/64064
#제재 아이디로 추정되는 아이디 목록 리턴
def checkBan(ban_id, user_id):
    ban_len = len(ban_id)
    same_id = set()
    for i in user_id:
        if len(i) == ban_len:
            for num in range(ban_len):
                if ban_id[num] != '*' and ban_id[num] != i[num]:
                    break
            else:
                same_id.add(i)
    return same_id

def solution(user_id, banned_id):
    ban_list = []
    ban_id_len = len(banned_id)
    #각 제재 아이디 당 해당할 수 있는 아이디 목록 추가 
    for ban_id in banned_id:
        temp = checkBan(ban_id, user_id)
        ban_list.append(temp)
    answer = set()
    def dfs(case, num, answer):
        if ban_id_len == num:
            answer.add(frozenset(case)) #정답 집합에 케이스 집합을 요소로 추가 추가
            return 0
        for ban_id in ban_list[num]:
            if ban_id not in case:
                case.add(ban_id)
                dfs(case, num + 1, answer)
                case.remove(ban_id)
    dfs(set(), 0, answer)
    
    return len(answer)
