def solution(players, callings):
    for i in range(len(callings)):
        for j in range(1,len(players)):
            if(callings[i]==players[j]):
                players[j-1], players[j] = players[j], players[j-1]
                break
    return players
