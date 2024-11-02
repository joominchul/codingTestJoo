#https://school.programmers.co.kr/learn/courses/30/lessons/72411
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for c in course:
        comb_counter = Counter()

        # 각 주문에 대해 조합을 생성하고 빈도 카운팅
        for order in orders:
            order = sorted(order) # 주문을 정렬하여 조합 생성의 일관성 유지
            comb_counter.update(combinations(order, c))  # 조합의 빈도 카운트

        # 가장 많이 주문된 조합의 주문수 추출
        max_count = 0
        for comb, count in comb_counter.items():
            if count > max_count and count >= 2:
                max_count = count

        # 최대 빈도수를 가진 조합을 추출
        answer += [''.join(comb) for comb, count in comb_counter.items() if count == max_count and count >= 2]

    return sorted(answer)
