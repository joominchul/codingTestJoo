#https://www.acmicpc.net/problem/15649
def dfs(n, m, seq):
    if m == 1:
        for i in range(1,n+1):
            if str(i) not in seq:
                print(seq + str(i))
    else:
        for i in range(1, n+1):
            if str(i) not in seq:
                dfs(n, m-1, seq + str(i) + " ")

n, m = input().split(" ")
dfs(int(n), int(m), "")
