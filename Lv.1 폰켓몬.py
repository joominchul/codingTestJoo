#https://school.programmers.co.kr/learn/courses/30/lessons/1845
def solution(nums):
    N2 = len(nums)//2
    numSet = set()
    for n in nums:
        numSet.add(n)
    if len(numSet) > N2:
        return N2
    else:
        return len(numSet)
