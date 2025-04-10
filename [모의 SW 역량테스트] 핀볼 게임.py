# 방향: 상, 하, 좌, 우
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 블록 반사 테이블 (블록 번호 1~5일 때 방향 전환)
BLOCK_REFLECT = [
    [],  # 0번은 없음
    [1, 3, 0, 2],  # 1번 블록
    [3, 0, 1, 2],  # 2번 블록
    [2, 0, 3, 1],  # 3번 블록
    [1, 2, 3, 0],  # 4번 블록
    [1, 0, 3, 2],  # 5번 블록 (벽 역할)
]

def simulate(y, x, d):
    ny, nx, direction = y, x, d
    score = 0
    while True:
        dy, dx = DIRECTIONS[direction]
        ny += dy
        nx += dx

        # 밖으로 나간 경우: 벽(5번 블록)처럼 반사
        if ny < 0 or ny >= n or nx < 0 or nx >= n:
            direction = BLOCK_REFLECT[5][direction]
            score += 1
            continue

        cell = board[ny][nx]

        # 시작점으로 돌아오면 종료
        if cell == -1:
            break

        # 블록 만남
        if 1 <= cell <= 5:
            direction = BLOCK_REFLECT[cell][direction]
            score += 1

        # 웜홀
        elif 6 <= cell <= 10:
            ny, nx = wormhole_dict[(ny, nx)]

        # 빈 공간이면 그냥 감 (cell == 0)
        # 아무 처리 필요 없음

    return score

# 테스트 케이스 수
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    
    # 웜홀 매핑: 위치 쌍 저장
    wormhole_dict = dict()
    for num in range(6, 11):
        positions = [(i, j) for i in range(n) for j in range(n) if board[i][j] == num]
        if len(positions) == 2:
            wormhole_dict[positions[0]] = positions[1]
            wormhole_dict[positions[1]] = positions[0]

    max_score = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                board[i][j] = -1  # 시작 지점 마킹
                for d in range(4):
                    score = simulate(i, j, d)
                    max_score = max(max_score, score)
                board[i][j] = 0  # 원상복구

    print(f"#{tc} {max_score}")
