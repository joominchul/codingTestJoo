# https://www.acmicpc.net/problem/9663

def place(row):  # row는 세로 깊이
    global result
    if row == n:
        result += 1     # global 또 까먹고 안 해줘서 오류남.
    else:
        for col in range(n):
            if not (cols[col] or pos_diagonals[row + col] or neg_diagonals[row - col]):
                cols[col] = True
                pos_diagonals[row + col] = True
                neg_diagonals[row - col] = True
                place(row + 1)
                cols[col] = False
                pos_diagonals[row + col] = False
                neg_diagonals[row - col] = False


n = int(input())
result = 0
cols, pos_diagonals, neg_diagonals = [False]*n, [False]*(2*n-1), [False]*(2*n-1)
place(0)
print(result)
