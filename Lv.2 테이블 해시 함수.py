def solution(data, col, row_begin, row_end):
    # 1. 정렬
    data.sort(key=lambda x: (x[col-1], -x[0]))
    
    # 2. S_i 계산 및 XOR 연산
    answer = 0
    for i in range(row_begin, row_end + 1):
        S_i = sum(num % i for num in data[i-1])
        answer ^= S_i  # XOR 연산
    
    return answer
