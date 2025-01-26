//https://school.programmers.co.kr/learn/courses/30/lessons/120831
class Solution {
    fun solution(n: Int): Int {
        var answer: Int = 0
        for (i in 2..n step 2) {
            answer += i
        }
        return answer
    }
}
