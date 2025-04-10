T = int(input())

# 상하좌우
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    mountain = []
    m_high = 0
    answer = 0

    for _ in range(N):
        row = list(map(int, input().split()))
        m_high = max(m_high, max(row))
        mountain.append(row)

    high_point = []
    for i in range(N):
        for j in range(N):
            if mountain[i][j] == m_high:
                high_point.append((i, j))

    visited = [[False]*N for _ in range(N)]

    def dfs(i, j, can_cut, length):
        global answer
        answer = max(answer, length)

        visited[i][j] = True
        current_height = mountain[i][j]

        for di, dj in direction:
            ni, nj = i + di, j + dj

            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                next_height = mountain[ni][nj]

                # 그냥 이동
                if next_height < current_height:
                    dfs(ni, nj, can_cut, length + 1)

                # 깎아서 이동 가능한 경우
                elif can_cut and next_height - K < current_height:
                    original = mountain[ni][nj]
                    for cut in range(1, K + 1):
                        if next_height - cut < current_height:
                            mountain[ni][nj] -= cut
                            dfs(ni, nj, False, length + 1)
                            mountain[ni][nj] = original  # 원복
                            break  # 한 번만 깎으면 되므로 break

        visited[i][j] = False  # 백트래킹

    for i, j in high_point:
        dfs(i, j, True, 1)

    print(f"#{test_case} {answer}")
