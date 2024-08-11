#https://www.acmicpc.net/problem/15652
def dfs(m, num, seq):
    if m == 1:
        for i in range(num, n+1):
            print(seq + str(i))
    else:
        for i in range(num, n+1):
            dfs(m-1, i, seq + str(i) + " ")
n, m = input().split(" ")
n = int(n)
dfs(int(m), 1, "")
